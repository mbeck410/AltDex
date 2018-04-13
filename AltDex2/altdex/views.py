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

from .models import Index, Coin, IndexPrice


def index(request):
    with open('./altdex/index.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def pullcurrent():
    print('!!!')
    coins = Coin.objects.order_by('name')
    indices = Index.objects.order_by('name')
    symbols = ''

    for coin in coins:
        symbols += coin.symbol + ','
    symbols = symbols[:-1]

    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols + '&tsyms=USD'
    r = requests.get(url)
    data = json.loads(r.text)

    coin_table = []
    coin_histories = {}

    for coin in coins:

        new_coin_history = {'coin': coin.name,
                            'symbol': coin.symbol,
                            'price': '{0:.2f}'.format(float(data['RAW'][coin.symbol]['USD']['PRICE'])),
                            'price_change': float('{0:.2f}'.format(data['RAW'][coin.symbol]['USD']['CHANGEDAY'])),
                            'price_percent_change': float('{0:.2f}'.format(data['RAW'][coin.symbol]['USD']['CHANGEPCTDAY'])),
                            'volume': float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H'])),
                            'market_cap': float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['MKTCAP'])),
                            'open': '{0:.2f}'.format(float(data['RAW'][coin.symbol]['USD']['OPENDAY'])),
                            'high': '{0:.2f}'.format(float(data['RAW'][coin.symbol]['USD']['HIGHDAY'])),
                            'low': '{0:.2f}'.format(float(data['RAW'][coin.symbol]['USD']['LOWDAY']))
                            }

        dict_entry = {coin.name: new_coin_history}

        coin_histories.update(dict_entry)

        coin_table.append(new_coin_history)


    for dex in indices:
        dex_coins = dex.coin_set.all()
        dex_market_cap = 0.0
        dex_price_change = 0.0

        for dex_coin in dex_coins:
            this_coin = coin_histories[dex_coin.name]
            dex_market_cap += this_coin['market_cap']
            dex_price_change += this_coin['price_change']


        dex_price = float(dex_market_cap) / float(dex.divisor)
        dex_percent_change = float(dex_market_cap) / float(dex.divisor * 100)

        new_dex_history = IndexPrice(   index=dex,
                                        price=dex_price,
                                        price_change=dex_price_change,
                                        price_percent_change=dex_percent_change,
                                        market_cap=dex_market_cap,
                                        divisor=dex.divisor
                                        )

        new_dex_history.save()

    return coin_table


def getindexall(request):
    indices = Index.objects.all()
    indices_all_output = []
    for dex in indices:
        dex_all = dex.indexprice_set.all()
        prices = []
        times = []
        for i in dex_all:
            prices.append(i.price)
            times.append(i.timestamp)

        index_dict = {'x': times, 'y': prices, 'fill': 'tozeroy', 'type': 'scatter'} #, 'mode': 'lines', 'line': {'color': '#ffffff'}}
                        # 'market_cap': float('{0:.0f}'.format(i.market_cap)),
                        # 'volume': float('{0:.0f}'.format(i.volume)),

        indices_all_output.append(index_dict)

    return JsonResponse({'dict_key': indices_all_output})


def getindexcurrent(request):
    indices = Index.objects.all()
    indices_current = []
    for dex in indices:
        dex_current = dex.indexprice_set.last()
        index_dict = {  'price': float('{0:.2f}'.format(dex_current.price)),
                        'price_percent': float('{0:.2f}'.format(dex_current.price_percent_change)),
                        'market_cap': float('{0:.0f}'.format(dex_current.market_cap)),
                        'time': str(dex_current.timestamp)
                        }

    indices_current.append(index_dict)

    return JsonResponse({'dict_key': indices_current})


def getcoinscurrent(request):
    coin_table = request.session.get('coin_table')
    return JsonResponse({'dict_key': coin_table})


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


rt = RepeatedTimer(30, pullcurrent) # it auto-starts, no need of rt.start()




