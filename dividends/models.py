from django.db import models
from uuid import uuid4

# Create your models here.

class Dividends(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    symbol = models.CharField(max_length=10)
    date = models.DateField()
    dividend_amount = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def year(self):
        return self.date.year