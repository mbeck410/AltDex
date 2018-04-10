from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from decimal import Decimal
import datetime
from threading import Timer
from time import sleep
import schedule
import sched
import time

import requests
import json

from .models import Index, Coin, CoinCurrent, CoinDay, IndexCurrent, IndexDay


def index(request):
    with open('./altdexapp/index.html') as file:
        contents = file.read()
    return HttpResponse(contents)


# View to create a daily CoinDay and IndexDay model from API data
def pulldaily(request):
    coins = Coin.objects.order_by('name')           # Make list of all coins
    indices = Index.objects.order_by('name')        # Make list of all indices
    symbols = ''                                    # Create string to add coin symbols to for API url

    # Loop over coins to add coin symbols to created string
    for coin in coins:
        symbols += coin.symbol + ','                # Add comma in between symbols for API url syntax
    symbols = symbols[:-1]                          # Remove last comma in string for API url syntax

    # Create url with coins symbols for API
    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols + '&tsyms=USD'

    # Make API request and convert JSON data into python dictionary
    r = requests.get(url)
    data = json.loads(r.text)

    # Loop over coins to create and save new CoinDay model and add API data
    for coin in coins:
        new_coin_day_history = CoinDay( coin=coin,
                                        open=data['RAW'][coin.symbol]['USD']['OPENDAY'],
                                        high=data['RAW'][coin.symbol]['USD']['HIGHDAY'],
                                        low=data['RAW'][coin.symbol]['USD']['LOWDAY']
                                        )

        new_coin_day_history.save()

    for dex in indices:
        dex_coin_list = dex.coin_set.all()
        dex_open = 0
        dex_high = 0
        dex_low = 0

        for dex_coin in dex_coin_list:
            coin_day = CoinDay.objects.get(coin=dex_coin, day=datetime.date.today())
            dex_open += coin_day.open
            dex_high += coin_day.high
            dex_low += coin_day.low

        new_dex_day = IndexDay( index=dex,
                                open=dex_open,
                                high=dex_high,
                                low=dex_low
                                )

        new_dex_day.save()

    return HttpResponse('ok')


def pullcurrent():
    coins = Coin.objects.order_by('name')
    indices = Index.objects.order_by('name')
    symbols = ''

    for coin in coins:
        symbols += coin.symbol + ','
    symbols = symbols[:-1]

    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols + '&tsyms=USD'
    r = requests.get(url)
    data = json.loads(r.text)

    for coin in coins:
        coin_day_history = CoinDay.objects.get(coin=coin, day=datetime.date.today())

        new_coin_history = CoinCurrent( coin=coin,
                                        price=data['RAW'][coin.symbol]['USD']['PRICE'],
                                        price_change=data['RAW'][coin.symbol]['USD']['CHANGEDAY'],
                                        price_percent_change=data['RAW'][coin.symbol]['USD']['CHANGEPCTDAY'],
                                        volume=data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H'],
                                        market_cap=data['RAW'][coin.symbol]['USD']['MKTCAP']
                                        )

        new_coin_history.save()

        # Check for new daily price high/low and update accordingly
        if new_coin_history.price > coin_day_history.high:
            coin_day_history.high = new_coin_history.price
            coin_day_history.save()

        if new_coin_history.price < coin_day_history.low:
            coin_day_history.low = new_coin_history.price
            coin_day_history.save()

    for dex in indices:
        dex_coins = dex.coin_set.all()
        dex_total_price = Decimal(0.0)
        dex_volume = Decimal(0.0)
        dex_market_cap = Decimal(0.0)

        for dex_coin in dex_coins:
            this_coin = Coin.objects.get(name=dex_coin)
            last_update = this_coin.coincurrent_set.latest('timestamp')
            dex_total_price += last_update.price
            dex_volume += last_update.volume
            dex_market_cap += last_update.market_cap

        dex_day_data = IndexDay.objects.get(index=dex, day=datetime.date.today())
        dex_price_change = Decimal(dex_total_price) - dex_day_data.open
        dex_percent_change = Decimal(dex_price_change) / dex_day_data.open

        new_dex_history = IndexCurrent( index=dex,
                                        price=dex_total_price,
                                        price_change=dex_price_change,
                                        price_percent_change=dex_percent_change,
                                        volume=dex_volume,
                                        market_cap=dex_market_cap
                                        )

        new_dex_history.save()

        if new_dex_history.price > dex_day_data.high:
            dex_day_data.high = new_dex_history.price
            dex_day_data.save()

        if new_dex_history.price < dex_day_data.low:
            dex_day_data.low = new_dex_history.price
            dex_day_data.save()

    # return HttpResponse('ok')


def getindexall(request):
    indices = Index.objects.all()
    indices_all_output = []
    for dex in indices:
        dex_all = dex.indexcurrent_set.all()
        prices = []
        times = []
        for i in dex_all:
            prices.append(i.price)
            times.append(i.timestamp)

        index_dict = {'x': times, 'y': prices, 'type': 'scatter'}
                        # 'market_cap': float('{0:.0f}'.format(i.market_cap)),
                        # 'volume': float('{0:.0f}'.format(i.volume)),




        indices_all_output.append(index_dict)

    return JsonResponse({'indices_all': indices_all_output})


def getindexcurrent(request):
    indices = Index.objects.all()
    indices_current = []
    for dex in indices:
        dex_current = dex.indexcurrent_set.last()
        index_dict = {  'price': float('{0:.2f}'.format(dex_current.price)),
                        'price_percent': float('{0:.2f}'.format(dex_current.price_percent_change)),
                        'market_cap': float('{0:.0f}'.format(dex_current.market_cap)),
                        'time': str(dex_current.timestamp)
                        }

    indices_current.append(index_dict)

    return JsonResponse({'indices_current': indices_current})


def getcoinscurrent(request):
    coins = Coin.objects.all()
    coins_current_output = []

    for coin in coins:
        coin_day = coin.coinday_set.last()
        coin_current = coin.coincurrent_set.last()
        coin_dict = {   'Symbol': str(coin_current.coin.symbol),
                        'Name': str(coin_current.coin),
                        'Market': float('{0:.0f}'.format(coin_current.market_cap)),
                        'Price': float('{0:.2f}'.format(coin_current.price)),
                        'Change': float('{0:.2f}'.format(coin_current.price_change)),
                        'percent': float('{0:.2f}'.format(coin_current.price_percent_change)),
                        'High': float('{0:.2f}'.format(coin_day.high)),
                        'Low': float('{0:.2f}'.format(coin_day.low)),
                        'Volume': float('{0:.0f}'.format(coin_current.volume))
                        }

        coins_current_output.append(coin_dict)

    return JsonResponse({'coins_current': coins_current_output})

# scheduler = sched.scheduler(time.time, time.sleep)
#
# def periodic(scheduler, interval, action):
#     scheduler.enter(interval, 5, periodic,
#                     (scheduler, interval, action))
#     pullcurrent
#
# periodic(scheduler, 30, pullcurrent())

# schedule.every(1).minutes.do(pullcurrent)
#
# while True:
#     schedule.run_pending()
#     time.sleep(10)


class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.function   = function
        self.interval   = interval
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False




# rt = RepeatedTimer(30, pullcurrent) # it auto-starts, no need of rt.start()



# try:
#     sleep(10) # your long-running job goes here...
# finally:
#     rt.stop() # better in a try/finally block to make sure the program ends!