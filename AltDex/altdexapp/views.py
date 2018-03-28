from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from datetime import datetime
import requests
import json

from .models import Index, Coin, CoinCurrent, CoinDay, IndexCurrent, IndexDay


def pulldaily(request):
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
        new_coin_day_history = CoinDay( coin=coin,
                                        open=data['RAW'][coin.symbol]['USD']['OPENDAY'],
                                        high=data['RAW'][coin.symbol]['USD']['HIGHDAY'],
                                        low=data['RAW'][coin.symbol]['USD']['LOWDAY'],
                                        )
        new_coin_day_history.save()

        for dex in indices:
            dex_coin_list = dex.coin_set.all()
            dex_open = 0
            dex_high = 0
            dex_low = 0
            if coin in dex_coin_list:
                dex_open += data['RAW'][coin.symbol]['USD']['OPENDAY']



    return HttpResponse('ok')


def pullcurrent(request):
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
        new_coin_history = CoinCurrent( coin=coin,
                                        price=data['RAW'][coin.symbol]['USD']['PRICE'],
                                        price_change=data['RAW'][coin.symbol]['USD']['CHANGEDAY'],
                                        price_percent_change=data['RAW'][coin.symbol]['USD']['CHANGEPCTDAY'],
                                        volume=data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H'],
                                        market_cap=data['RAW'][coin.symbol]['USD']['MKTCAP'],
                                        timestamp=datetime.now())

        new_coin_history.save()

    # for dex in indices:
    #     dex_coins = dex.coin_set.all()
    #     dex_total_price = 0
    #     dex_volume = 0
    #     dex_market_cap = 0
    #
    #     for dex_coin in dex_coins:
    #         this_coin = Coin.objects.get(name=dex_coin)
    #         last_update = this_coin.coincurrent_set.latest('timestamp')
    #         dex_total_price += last_update.price
    #         dex_volume += last_update.volume
    #         dex_market_cap += last_update.market_cap
    #
    #
    #     new_index_history = IndexCurrent



    return HttpResponse('ok')

