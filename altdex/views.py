from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
# from django.urls import reverse
# from decimal import Decimal
# import datetime
# from threading import Timer
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


def pullcurrent(request):
    if request.user.is_superuser:
        coin_table = collect()
        request.session['coin_table'] = coin_table
        return render(request, 'pullcurrent.html')
    else:
        return HttpResponse('error')


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

        index_dict = {'x': times, 'y': prices, 'fill': 'tozeroy', 'type': 'scatter', 'line': {'color': '#244ec3'},  'mode': 'lines'}
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
                        'change_24h': float('{0:.2f}'.format(dex_current.change_24h)),
                        'price_percent': float('{0:.2f}'.format(dex_current.price_percent_change)),
                        'market_cap': float('{0:.0f}'.format(dex_current.market_cap)),
                        'time': str(dex_current.timestamp)
                        }

        indices_current.append(index_dict)

    print(indices_current[0])

    return JsonResponse({'dict_key': indices_current})


def getcoinscurrent(request):
    coin_table = request.session.get('coin_table')
    if not coin_table:
        coin_table = collect(request)
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


# rt = RepeatedTimer(30, pullcurrent) # it auto-starts, no need of rt.start()




