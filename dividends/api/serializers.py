from rest_framework import serializers
from dividends import models


class DividendsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dividends
        fields = "__all__"
