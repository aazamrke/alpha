from django.db import models

# Create your models here.


class Quote(models.Model):
    from_currency_code = models.CharField(max_length=50)
    from_currency_name = models.CharField(max_length=50)
    to_currency_code = models.CharField(max_length=50)
    to_currency_name = models.CharField(max_length=50)
    exchange_rate = models.FloatField()
    last_refreshed = models.DateTimeField()
    time_zone = models.CharField(max_length=50)
    bid_price = models.FloatField()
    ask_price = models.FloatField()

    def __str__(self):
        return self.from_currency_code

    class Meta:
        ordering = ['-last_refreshed']