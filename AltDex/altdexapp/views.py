from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
import requests
import json

from .models import Index, Coin


def index(request):
    index_name = Index.objects.get(pk=1)
    coins = index_name.coin_set.all()
    symbols = ''
    for coin in coins:

        symbols += coin.symbol
        print(type(symbols))
    print(symbols)
    # url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,CAPP&tsyms=USD'
    # for coin in coins:
    #     # symbol = coin.symbol
    #     # url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,CAPP&tsyms=USD'
    #     r = requests.get(url)
    #     data = json.loads(r.text)
    #     print(data['RAW']['FROMSYMBOL'] + ': ' + str(data['RAW']['PRICE']))
    return HttpResponse(coins)

