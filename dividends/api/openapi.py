from typing import List, Optional
from dividends.models import Dividends
from ninja import Router
from ninja.orm import create_schema

router = Router()

DividendsSchemaIn = create_schema(Dividends, exclude=["id"])

DividendsSchemaOut = create_schema(Dividends)

@router.get("/dividends/", response=List[DividendsSchemaOut])
def list_all_dividends(request):
    return list(Dividends.objects.all())


@router.get("/dividends/filter/", response=List[DividendsSchemaOut])
def filter_dividends(request, symbol: Optional[str] = None, year: Optional[int] = None):
    query_params = {}
    if symbol:
        query_params["symbol"] = symbol
    if year:
        query_params["date__year"] = year

    dividends = Dividends.objects.filter(**query_params)

    if year:
        dividends = [dividend for dividend in dividends if dividend.year == year]

    return list(dividends)
