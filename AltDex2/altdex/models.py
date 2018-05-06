from django.db import models
import datetime


class Index(models.Model):
    name = models.CharField(max_length=20)
    divisor = models.DecimalField(max_digits=50, decimal_places=25)

    def __str__(self):
        return self.name


class Coin(models.Model):
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=5)
    indices = models.ManyToManyField(Index)
    api = models.CharField(max_length=25, default='CryptoCompare')
    coin_marketcap_id = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class IndexPrice(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    price_percent_change = models.DecimalField(max_digits=50, decimal_places=25)
    market_cap = models.DecimalField(max_digits=50, decimal_places=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    divisor = models.DecimalField(max_digits=50, decimal_places=25)

    def __str__(self):
        return self.index.name + ' - ' + str(self.timestamp)