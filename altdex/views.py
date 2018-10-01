from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from datetime import timedelta
# from django.urls import reverse
# from decimal import Decimal
# from datetime
# from threading import Timer
# from time import sleep
# import schedule
# import sched
# import time

import requests
import json
from .helpers import collect
from .models import Index, Coin, IndexPrice

# month_index = 0
# week_index = 0
# week_high_index = 0
# week_low_index = 0
# month_high_index = 0
# month_low_index = 0


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

def masternode(request):
    with open('./altdex/masternode.html') as file:
        contents = file.read()
    return HttpResponse(contents)

def about(request):
    with open('./altdex/about.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def privacy_policy(request):
    with open('./altdex/privacy_policy.html') as file:
        contents = file.read()
    return HttpResponse(contents)


def pullcurrent(request):
    if request.user.is_superuser:
        test = collect()
        return render(request, 'pullcurrent.html')
    else:
        return HttpResponse('error')


def testing(request):
    if request.user.is_superuser:
        with open('./altdex/testing.html') as file:
            contents = file.read()
            return HttpResponse(contents)
    else:
        return HttpResponse('error')


def getindexall(request):
    indices = Index.objects.order_by('id')
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
    indices = Index.objects.order_by('id')
    indices_current = []

    for dex in indices:
        if dex.name != 'Null':
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
            elif dex.name == 'Masternode':
                link = '/masternode'
                symbol = 'ALTMSN'

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
    coins = Coin.objects.order_by('market_cap')
    coin_table = []
    weight_1 = 0
    weight_2 = 0
    weight_3 = 0
    weight_4 = 0

    for this_coin in coins:
        # percent_weight = '{0:.3f}'.format(float(this_coin.market_cap) / (float(index.market_cap))*100)

        dices = ''
        indices_in = this_coin.indices.all()

        for dex in indices_in:

            if dex.name == 'AltDex100':
                weight_1 = this_coin.market_cap/dex.indexprice_set.last().market_cap * 100
                dices += str(dex.name)
                if weight_1 >= 1:
                    weight_1 = float('{0:.3f}'.format(weight_1))
                else:
                    weight_1 = float('{0:.6f}'.format(weight_1))
            if dex.name == 'Exchange':
                weight_2 = this_coin.market_cap/dex.indexprice_set.last().market_cap * 100
                dices += str(dex.name)
                if weight_2 >= 1:
                    weight_2 = float('{0:.3f}'.format(weight_2))
                else:
                    weight_2 = float('{0:.6f}'.format(weight_2))
            if dex.name == 'Privacy':
                weight_3 = this_coin.market_cap / dex.indexprice_set.last().market_cap * 100
                dices += str(dex.name)
                if weight_3 >= 1:
                    weight_3 = float('{0:.3f}'.format(weight_3))
                else:
                    weight_3 = float('{0:.6f}'.format(weight_3))
            if dex.name == 'Masternode':
                weight_4 = this_coin.market_cap / dex.indexprice_set.last().market_cap * 100
                dices += str(dex.name)
                if weight_4 >= 1:
                    weight_4 = float('{0:.3f}'.format(weight_4))
                else:
                    weight_4 = float('{0:.6f}'.format(weight_4))
            else:
                continue

        if float(this_coin.price) >= 1:
            coin_price = '{:,.2f}'.format(float(this_coin.price))
        else:
            coin_price = '{0:.6f}'.format(float(this_coin.price))

        name_lower = str(this_coin.name).lower()
        if name_lower == 'metaverse ep':
            coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/metaverse.png'

        elif name_lower == 'stakenet':
            coin_icon_url = 'https://s2.coinmarketcap.com/static/img/coins/16x16/2633.png'

        elif name_lower == 'airswap':
            coin_icon_url = 'https://s2.coinmarketcap.com/static/img/coins/16x16/2058.png'

        elif name_lower == 'horizen':
            coin_icon_url = 'https://s2.coinmarketcap.com/static/img/coins/16x16/1698.png'

        elif name_lower == 'ambrosus':
            coin_icon_url = 'https://s2.coinmarketcap.com/static/img/coins/16x16/2081.png'

        elif ' ' in name_lower:
            hyphened_name = name_lower.replace(' ', '-')
            coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/' + hyphened_name + '.png'

        else:
            no_space = name_lower.replace(' ', '')

            if no_space == 'bytecoin':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/'+no_space+'-bcn.png'
            elif no_space == 'navcoin':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/nav-coin.png'
            elif no_space == 'bitcoinprivate':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/bitcoin-private.png'
            elif no_space == 'golem':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/golem-network-tokens.png'
            elif no_space == 'iost':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/iostoken.png'
            elif no_space == 'nebulas':
                coin_icon_url = 'https://raw.githubusercontent.com/dziungles/cryptocurrency-logos/master/coins/16x16/nebulas-token.png'
            elif no_space == 'bibox':
                coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/bibox-token.png'
            elif no_space == 'polymath':
                coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/polymath-network.png'
            # elif no_space == 'metaverseep':
            #     coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/metaverse.png'
            else:
                coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/'+no_space+'.png'

        #

        #
        # if no_space == 'cortex':
        #     coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/cortex.png'
        #
        # if no_space == 'switcheo':
        #     coin_icon_url = 'https://files.bitscreener.com/static/img/coins/16x16/switcheo.png'


        coin_dict = {   'name': this_coin.name,
                        'website': this_coin.website,
                        'symbol': this_coin.symbol,
                        'market_cap': float('{0:.0f}'.format(this_coin.market_cap)),
                        'pretty_price': coin_price,
                        'price': float(this_coin.price),
                        'price_percent': float('{0:.2f}'.format(this_coin.price_percent_change)),
                        'volume': float('{0:.0f}'.format(this_coin.volume)),
                        'indices': dices,
                        'weight_1': weight_1,
                        'weight_2': weight_2,
                        'weight_3': weight_3,
                        'weight_4': weight_4,
                        'icon': coin_icon_url
                        }

        coin_table.append(coin_dict)


    return JsonResponse({'dict_key': coin_table})


def getindexperformance(request):
    performance_table = []
    indices = Index.objects.order_by('id')
    for index in indices:

        if index.name != 'Null':
            entries = index.indexprice_set.order_by('-timestamp')
            entries2 = index.indexprice_set.order_by('timestamp')
            latest_entry = entries[0]

            current_price = latest_entry.price
            current_date = latest_entry.timestamp
            current_seconds = current_date.second
            currrent_microseconds = current_date.microsecond

            week_change = 0.0
            month_change = 0.0
            week_percent = 0.0
            month_percent = 0.0
            day_low = current_price
            day_high = current_price
            week_low = current_price
            week_high = current_price
            month_high = current_price
            month_low = current_price

            one_day = current_date - timedelta(days=1, seconds=current_seconds, microseconds=currrent_microseconds)
            one_m = current_date - timedelta(days=31, seconds=current_seconds, microseconds=currrent_microseconds)
            seven = current_date - timedelta(days=7, seconds=current_seconds, microseconds=currrent_microseconds)

            for i in range(0, len(entries)):
                if entries[i].price > month_high:
                    month_high = entries[i].price
                    # month_high_index = i

                if entries[i].price < month_low:
                    month_low = entries[i].price
                    # month_low_index = i

                last_time = entries[i].timestamp
                last_seconds = last_time.second
                last_micro = last_time.microsecond
                strip_time = last_time - timedelta(seconds=last_seconds, microseconds=last_micro)

                if strip_time == one_day:
                    day_high = month_high
                    day_low = month_low

                if i > 1300:
                    if day_high == day_low:
                        day_high = month_high
                        day_low = month_low

                if strip_time == seven:
                    week_change = current_price - entries[i].price
                    week_index = i
                    week_high = month_high
                    week_low = month_low
                    week_percent = week_change / entries[i].price * 100
                    # week_high_index = month_high_index
                    # week_low_index = month_low_index

                if i > 9000:
                    if week_high == week_low:
                        week_change = current_price - entries[8660].price
                        week_percent = week_change / entries[8660].price * 100
                        week_high = month_high
                        week_low = month_low

                if strip_time == one_m:
                    month_change = current_price - entries[i].price
                    month_index = i
                    month_percent = month_change / entries[i].price * 100
                    break

                if i > 35000:
                    # week_change = current_price - entries[8660].price
                    month_change = current_price - entries[32600].price
                    # week_percent = week_change / entries[8660].price * 100
                    month_percent = month_change / entries[32600].price * 100
                    # week_high = entries[week_high_index].price
                    # week_low = entries[week_low_index].price
                    # week_high = '-'
                    # week_low = '-'
                    break

            change_dict = { 'current': current_price,
                            'week': week_change,
                            'month': one_m,
                            'month_change': month_change,
                            # 'week_index': week_index,
                            # 'month_index':month_index,
                            'week_high': week_high,
                            'week_low': week_low,
                            'month_high': month_high,
                            'month_low':month_low,
                            'day_high': day_high,
                            'day_low': day_low,
                            'month_percent': '{0:.2f}'.format(month_percent),
                            'week_percent': '{0:.2f}'.format(week_percent),
                        }

            performance_table.append(change_dict)

        else: continue

    return JsonResponse({'dict_key': performance_table})

def gainers_losers(request):
    indices = Index.objects.order_by('id')
    loser_array = []
    gainer_array = []

    for index in indices:
        losers = index.coin_set.order_by('price_percent_change')[:5]
        gainers = index.coin_set.order_by('-price_percent_change')[:5]
        loser_index_array = []
        gainer_index_array = []


        for loser_coin in losers:

            if float(loser_coin.price) >= 1:
                coin_price = '{:,.2f}'.format(float(loser_coin.price))
            else:
                coin_price = '{0:.6f}'.format(float(loser_coin.price))

            losers_dict = { 'symbol': loser_coin.symbol,
                            'website': loser_coin.website,
                            'price': coin_price,
                            'price_percent': '{:,.2f}'.format(float(loser_coin.price_percent_change))}

            loser_index_array.append(losers_dict)

        loser_array.append(loser_index_array)

        for gainer_coin in gainers:

            if float(gainer_coin.price) >= 1:
                coin_price = '{:,.2f}'.format(float(gainer_coin.price))
            else:
                coin_price = '{0:.6f}'.format(float(gainer_coin.price))

            gainers_dict = {'symbol': gainer_coin.symbol,
                            'website': gainer_coin.website,
                            'price': coin_price,
                            'price_percent': '{:,.2f}'.format(float(gainer_coin.price_percent_change))}

            gainer_index_array.append(gainers_dict)

        gainer_array.append(gainer_index_array)

    return JsonResponse({'losers': loser_array, 'gainers': gainer_array})
    # 'gainers': gainer_array,

def rsi_calc(request):
    day = 0
    displayed_prices = []
    index = Index.objects.get(name="AltDex100")
    prices = index.indexprice_set.order_by('timestamp')
    new_prices = prices.filter(timestamp__hour=19)
    for price in new_prices:
        this_day = price.timestamp.day
        day_diff = abs(this_day - day)

        if day_diff == 2:
            missing_day = price.timestamp - timedelta(days=1)
            missing_price = price.price - price.change_24h
            s_info = {'date' :missing_day,
                      'price': missing_price}

            displayed_prices.append(s_info)

        if this_day != day:
            info = {'date': price.timestamp,
                    'price': price.price}

            displayed_prices.append(info)
            day = this_day

    # gain = 0
    # lose = 0
    # avg_gain = 0
    # avg_lose = 0
    # rsi_values = []
    # times = []
    # twelve_ema = []
    # twelve_ema_times = []
    # twentysix_ema = []
    # twentysix_ema_times = []
    #
    # 12 Day EMA
    test = []
    period = 12
    multiplier = float(2 / (period + 1))
    sum = 0
    sma = 0

    for j in range(len(displayed_prices)):
        if j <= period:
            sum += displayed_prices[j]['price']
            # test.append(sum)

        elif j == (period + 1):
            sma = float(sum) / float(period)
            ema = ((float(displayed_prices[j]['price']) - float(sma)) * multiplier) + float(sma)
            test.append(ema)
            test.append(displayed_prices[j]['date'])

        else:
            ema = ((float(displayed_prices[j]['price']) - float(ema)) * multiplier) + float(ema)
            # twelve_ema.append(ema)
            # twelve_ema_times.append(displayed_prices[j]['date'])
            test.append(ema)
            test.append(displayed_prices[j]['date'])


    # RSI Calculation
    # for i in range(1, len(displayed_prices)):
    #     this_price_change = displayed_prices[i]['price'] - displayed_prices[i-1]['price']
    #
    #     rs_value = 0
    #     rsi_value = 0
    #
    #     if i < 14:
    #         if this_price_change >= 0:
    #             gain += this_price_change
    #         else:
    #             lose += abs(this_price_change)
    #
    #     elif i == 14:
    #
    #         if this_price_change >= 0:
    #             gain += this_price_change
    #         else:
    #             lose += abs(this_price_change)
    #
    #         avg_gain = float(gain) / 14
    #         avg_lose = float(lose) / 14
    #
    #         rs_value = float(avg_gain) / float(avg_lose)
    #         rsi_value = 100 - (100 / (1 + float(rs_value)))
    #
    #         rsi_values.append(rsi_value)
    #         times.append(displayed_prices[i]['date'])
    #
    #     else:
    #         this_gain = 0
    #         this_lose = 0
    #
    #         if this_price_change >= 0:
    #             this_gain = this_price_change
    #
    #         else:
    #             this_lose = abs(this_price_change)
    #
    #
    #         avg_gain = ((float(avg_gain) * (13)) + float(this_gain)) / 14
    #         avg_lose = ((float(avg_lose) * (13)) + float(this_lose)) / 14
    #
    #
    #         rs_value = float(avg_gain) / float(avg_lose)
    #
    #         rsi_value = 100 - (100 / (1 + float(rs_value)))
    #
    #         rsi_values.append(rsi_value)
    #         times.append(displayed_prices[i]['date'])

    # index_dict = []

    # index_dict1 = {'x': times, 'y': rsi_values, 'type': 'scatter', 'yaxis': 'y2',  'mode': 'lines'}
    # index_dict2 = {'x': twelve_ema_times, 'y': twelve_ema, 'type': 'scatter', 'yaxis': 'y2',  'mode': 'lines'}

    # index_dict.append(index_dict1)
    # index_dict.append(index_dict2)

    return JsonResponse({'prices': test})

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
