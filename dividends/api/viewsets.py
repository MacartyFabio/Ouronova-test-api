from rest_framework import viewsets
from dividends import models
from dividends.api import serializers


class DividendsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DividendsSerializer
    queryset = models.Dividends.objects.all()
