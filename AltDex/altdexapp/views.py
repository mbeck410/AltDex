from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse
from decimal import Decimal
import datetime

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

    return HttpResponse('ok')


def getindexcurrent(request):
    indices = Index.objects.all()
    indices_current_output = []
    for dex in indices:
        dex_current = dex.indexcurrent_set.last()
        indices_current_output.append(dex_current.toDict())

    return JsonResponse({'indices_current': indices_current_output})


def getindexday(request):
    indices = Index.objects.all()
    indices_day_output = []
    for dex in indices:
        dex_day = dex.indexday_set.last()
        indices_day_output.append(dex_day.toDict())

    return JsonResponse({'indices_day': indices_day_output})


def getcoinscurrent(request):
    coins = Coin.objects.all()
    coins_current_output = []

    for coin in coins:
        coin_day = coin.coinday_set.last()
        coin_current = coin.coincurrent_set.last()
        coin_dict = {   'Symbol': str(coin_current.coin.symbol),
                        'Name': str(coin_current.coin),
                        'Market': float("{0:.0f}".format(coin_current.market_cap)),
                        'Price': float("{0:.2f}".format(coin_current.price)),
                        'Change': float("{0:.2f}".format(coin_current.price_change)),
                        '%Chg': float("{0:.2f}".format(coin_current.price_percent_change)),
                        'High': float("{0:.2f}".format(coin_day.high)),
                        'Low': float("{0:.2f}".format(coin_day.low)),
                        'Volume': float("{0:.0f}".format(coin_current.volume))
                        }

        coins_current_output.append(coin_dict)

    return JsonResponse({'coins_current': coins_current_output})


def getcoinsday(request):
    coins = Coin.objects.all()
    coins_day_output = []
    for coin in coins:
        coin_day = coin.coinday_set.last()
        coins_day_output.append(coin_day.toDict())

    return JsonResponse({'coins_day': coins_day_output})


