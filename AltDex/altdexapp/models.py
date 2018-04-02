from django.db import models
import datetime


class Index(models.Model):
    name = models.CharField(max_length=20)
    divisor = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return self.name


class Coin(models.Model):
    name = models.CharField(max_length=25)
    symbol = models.CharField(max_length=5)
    indices = models.ManyToManyField(Index)

    def __str__(self):
        return self.name


class CoinCurrent(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    price_change = models.DecimalField(max_digits=50, decimal_places=25)
    price_percent_change = models.DecimalField(max_digits=50, decimal_places=25)
    volume = models.DecimalField(max_digits=50, decimal_places=25)
    market_cap = models.DecimalField(max_digits=50, decimal_places=25)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coin.name + ' - ' + str(self.timestamp)

    def pretty_price_change(self):
        return '{0:.2f}'.format(self.price_change)

    def pretty_price_percent_change(self):
        return '{0:.2f}'.format(self.price_percent_change)

    def pretty_volume(self):
        return '{0:.0f}'.format(self.volume)

    def pretty_market_cap(self):
        return '{0:.0f}'.format(self.market_cap)

    def toDict(self):
        return {'id':self.id, 'coin':self.coin, 'price':self.price, 'price_change':self.pretty_price_change,
                'price_percent':self.pretty_price_percent_change, 'volume':self.pretty_volume,
                'market_cap':self.pretty_market_cap}


class IndexCurrent(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=25, decimal_places=2)
    price_change = models.DecimalField(max_digits=50, decimal_places=25)
    price_percent_change = models.DecimalField(max_digits=50, decimal_places=25)
    volume = models.DecimalField(max_digits=50, decimal_places=25)
    market_cap = models.DecimalField(max_digits=50, decimal_places=25)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.index.name + ' - ' + str(self.timestamp)

    def __str__(self):
        return self.coin.name + ' - ' + str(self.timestamp)

    def pretty_price_change(self):
        return '{0:.2f}'.format(self.price_change)

    def pretty_price_percent_change(self):
        return '{0:.2f}'.format(self.price_percent_change)

    def pretty_volume(self):
        return '{0:.0f}'.format(self.volume)

    def pretty_market_cap(self):
        return '{0:.0f}'.format(self.market_cap)

    def toDict(self):
        return {'id': self.id, 'index': self.index, 'price': self.price, 'price_change': self.pretty_price_change,
                'price_percent': self.pretty_price_percent_change, 'volume': self.pretty_volume,
                'market_cap': self.pretty_market_cap}


class CoinDay(models.Model):
    coin = models.ForeignKey(Coin, on_delete=models.CASCADE)
    open = models.DecimalField(max_digits=50, decimal_places=25)
    high = models.DecimalField(max_digits=50, decimal_places=25)
    low = models.DecimalField(max_digits=50, decimal_places=25)
    day = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.coin.name + ' - ' + str(self.day)

    def pretty_open(self):
        return '{0:.2f}'.format(self.open)

    def pretty_high(self):
        return '{0:.2f}'.format(self.high)

    def pretty_low(self):
        return '{0:.2f}'.format(self.low)

    def toDict(self):
        return {'id': self.id, 'coin': self.coin, 'open':self.pretty_open, 'high':self.pretty_high, 'low':self.pretty_low}


class IndexDay(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    open = models.DecimalField(max_digits=50, decimal_places=25)
    high = models.DecimalField(max_digits=50, decimal_places=25)
    low = models.DecimalField(max_digits=50, decimal_places=25)
    day = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.index.name + ' - ' + str(self.day)

    def pretty_open(self):
        return '{0:.2f}'.format(self.open)

    def pretty_high(self):
        return '{0:.2f}'.format(self.high)

    def pretty_low(self):
        return '{0:.2f}'.format(self.low)

    def toDict(self):
        return {'id': self.id, 'index': self.index, 'open':self.pretty_open, 'high':self.pretty_high, 'low':self.pretty_low}




