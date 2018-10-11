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
    price = models.DecimalField(max_digits=25, decimal_places=10)
    change_24h = models.DecimalField(max_digits=25, decimal_places=2)
    price_percent_change = models.DecimalField(max_digits=50, decimal_places=25)
    market_cap = models.DecimalField(max_digits=50, decimal_places=25)
    volume = models.DecimalField(max_digits=50, decimal_places=25)
    percent_weight = models.DecimalField(max_digits=50, decimal_places=25)
    website = models.CharField(max_length=50, default='')

    def __str__(self):

        return self.name


class IndexPrice(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    change_24h = models.DecimalField(max_digits=25, decimal_places=2)
    price_percent_change = models.DecimalField(max_digits=50, decimal_places=25)
    market_cap = models.DecimalField(max_digits=50, decimal_places=25)
    timestamp = models.DateTimeField(auto_now_add=True)
    divisor = models.DecimalField(max_digits=50, decimal_places=25)

    def __str__(self):
        return self.index.name + ' - ' + str(self.timestamp)

class IndexDay(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    day_high = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    day_low = models.DecimalField(max_digits=20, decimal_places=2, default=0.0)
    rsi = models.DecimalField(max_digits=10, decimal_places=5, default=0.0)
    sma_12 = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    sma_26 = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    ema_12 = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    ema_26 = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    macd = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    macd_trend = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    fib = models.DecimalField(max_digits=20, decimal_places=10, default=0.0)
    day = models.DateTimeField(auto_now_add=False)

    def __str__(self):

        return self.index.name + ' - ' + str(self.timestamp)
