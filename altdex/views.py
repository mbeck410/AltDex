from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.urls import reverse
# from decimal import Decimal
# import datetime
from threading import Timer
# from time import sleep
# import schedule
# import sched
# import time

import requests
import json
from .helpers import collect
from .models import Index, Coin, IndexPrice


def altdex(request):
    with open('./altdex/altdex.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def exchange(request):
    with open('./altdex/exchange.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def privacy(request):
    with open('./altdex/privacy.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def about(request):
    with open('./altdex/about.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def privacy_policy(request):
    with open('./altdex/p_policy.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def pullcurrent(request):
    if request.user.is_superuser:
        test = collect()
        return render(request, 'pullcurrent.html')
    else:
        return HttpResponse('error')


def getindexall(request):
    indices = Index.objects.all()
    indices_all_output = []
    for dex in indices:
        dex_price_entries = dex.indexprice_set.order_by('timestamp')
        prices = []
        times = []
        for i in dex_price_entries:
            prices.append(i.price)
            times.append(i.timestamp)

        index_dict = {'x': times, 'y': prices, 'fill': 'tozeroy', 'type': 'scatter', 'line': {'color': '#6dc0eb'},  'mode': 'lines'}
                        # 'market_cap': float('{0:.0f}'.format(i.market_cap)),
                        # 'volume': float('{0:.0f}'.format(i.volume)),

        indices_all_output.append(index_dict)


    return JsonResponse({'dict_key': indices_all_output})


def getindexcurrent(request):
    indices = Index.objects.all()
    indices_current = []
    for dex in indices:
        link = ''
        if dex.name == 'AltDex100':
            link = '/'
            symbol = 'ALT100'
        elif dex.name == 'Exchange':
            link = '/exchange'
            symbol = 'ALTEXC'
        elif dex.name == 'Privacy':
            link = '/privacy'
            symbol = 'ALTPRV'

        dex_current = dex.indexprice_set.last()
        index_dict = {  'link': link,
                        'name': dex.name,
                        'price': float('{0:.2f}'.format(dex_current.price)),
                        'change_24h': float('{0:.2f}'.format(dex_current.change_24h)),
                        'price_percent': float('{0:.2f}'.format(dex_current.price_percent_change)),
                        'market_cap': float('{0:.0f}'.format(dex_current.market_cap)),
                        'time': str(dex_current.timestamp),
                        'symbol': symbol
                        }

        indices_current.append(index_dict)

    return JsonResponse({'dict_key': indices_current})


def getcoinscurrent(request):
    coins = Coin.objects.all()
    coin_table = []
    weight_1 = 0
    weight_2 = 0
    weight_3 = 0

    for this_coin in coins:
        # percent_weight = '{0:.3f}'.format(float(this_coin.market_cap) / (float(index.market_cap))*100)

        dices = ''
        indices_in = this_coin.indices.all()


        for dex in indices_in:
            dices += str(dex.name)
            if dex.name == 'AltDex100':
                weight_1 = this_coin.market_cap/dex.indexprice_set.last().market_cap * 100
                if weight_1 >= 1:
                    weight_1 = format(float(weight_1), '.3f')
                else:
                    weight_1 = float('{0:.6f}'.format(weight_1))
            if dex.name == 'Exchange':
                weight_2 = this_coin.market_cap/dex.indexprice_set.last().market_cap * 100
                if weight_2 >= 1:
                    weight_2 = format(float(weight_2), '.3f')
                else:
                    weight_2 = float('{0:.6f}'.format(weight_2))
            if dex.name == 'Privacy':
                weight_3 = this_coin.market_cap / dex.indexprice_set.last().market_cap * 100
                if weight_3 >= 1:
                    weight_3 = format(float(weight_3), '.3f')
                else:
                    weight_3 = float('{0:.6f}'.format(weight_3))

        if float(this_coin.price) >= 1:
            coin_price = float('{0:.2f}'.format(this_coin.price))
        else:
            coin_price = float('{0:.6f}'.format(this_coin.price))

        coin_dict = {   'name': this_coin.name,
                        'symbol': this_coin.symbol,
                        'market_cap': float('{0:.0f}'.format(this_coin.market_cap)),
                        'price': float(coin_price),
                        'price_percent': float('{0:.2f}'.format(this_coin.price_percent_change)),
                        'volume': float('{0:.0f}'.format(this_coin.volume)),
                        'indices': dices,
                        'weight_1': weight_1,
                        'weight_2': weight_2,
                        'weight_3': weight_3
                        }

        coin_table.append(coin_dict)


    return JsonResponse({'dict_key': coin_table})


# class RepeatedTimer(object):
#     def __init__(self, interval, function, *args, **kwargs):
#         self._timer     = None
#         self.function   = function
#         self.interval   = interval
#         self.args       = args
#         self.kwargs     = kwargs
#         self.is_running = False
#         self.start()
#
#     def _run(self):
#         self.is_running = False
#         self.start()
#         self.function(*self.args, **self.kwargs)
#
#     def start(self):
#         if not self.is_running:
#             self._timer = Timer(self.interval, self._run)
#             self._timer.start()
#             self.is_running = True
#
#     def stop(self):
#         self._timer.cancel()
#         self.is_running = False
#
#
# rt = RepeatedTimer(30, collect) # it auto-starts, no need of rt.start()




