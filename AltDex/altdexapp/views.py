from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
import requests
import json

from .models import Index, Coin, CoinCurrent, CoinDay, IndexCurrent, IndexDay


def index(request):
    coins = Coin.objects.order_by('name')
    indices = Index.objects.order_by('name')
    # symbols = ''
    # for coin in coins:
    #     symbols += coin.symbol + ','
    # symbols = symbols[:-1]
    #
    # url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols + '&tsyms=USD'
    # r = requests.get(url)
    # data = json.loads(r.text)
    #
    # for coin in coins:
    #     new_coin_history = CoinCurrent( coin=coin,
    #                                     price=data['RAW'][coin.symbol]['USD']['PRICE'],
    #                                     price_change=data['RAW'][coin.symbol]['USD']['CHANGEDAY'],
    #                                     price_percent_change=data['RAW'][coin.symbol]['USD']['CHANGEPCTDAY'],
    #                                     volume=data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H'],
    #                                     market_cap=data['RAW'][coin.symbol]['USD']['MKTCAP'],
    #                                     timestamp=datetime.now())
    #
    #     new_coin_history.save()

    for dex in indices:
        dex_coins = dex.coin_set.all()
        # total_price = 0
        # dex_volume = 0
        # dex_market_cap = 0
        for dex_coin in dex_coins:
            this_coin = CoinCurrent.objects.order_by(coin=dex_coin,
            coin_data = this_coin.objects.last()
            #total_price += dex_coin.price
            print(str(coin_data.price) + ' ' + str(coin_data.coin.name))
        new_index_history = IndexCurrent



    return HttpResponse(coins)

