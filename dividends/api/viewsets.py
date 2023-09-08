from rest_framework import viewsets
from rest_framework.response import Response
from dividends import models
from dividends.api import serializers

class DividendsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DividendsSerializer
    queryset = models.Dividends.objects.all()
    def list(self, request):
        symbol = request.query_params.get('symbol')
        year = request.query_params.get('year')

        if symbol and year:
            dividends = models.Dividends.objects.filter(symbol=symbol, date__year=year)
        else:
            dividends = models.Dividends.objects.all()

        serializer = serializers.DividendsSerializer(dividends, many=True)
        return Response(serializer.data)
