from ninja import Router
from typing import List
from django.shortcuts import get_object_or_404
from dividends.models import Dividends
from ninja.orm import create_schema
from uuid import UUID

router = Router()

# Na entrada, o id será criado automáticamente
DividendsSchemaIn = create_schema(Dividends, exclude=["id"])

# Na saída, o id deve ser mostrado
DividendsSchemaOut = create_schema(Dividends)


@router.post("")
def register_dividends(request, event: DividendsSchemaIn):
    Dividends.objects.create(**event.dict())
    return event


@router.get("", response=List[DividendsSchemaOut])
def list_dividends(request):
    return list(Dividends.objects.all())


@router.get("/{id}", response=DividendsSchemaIn)
def dividends_id(request, id: UUID):
    return get_object_or_404(Dividends, id=UUID)