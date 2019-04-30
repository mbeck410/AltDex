import requests
import json
from time import sleep
from datetime import timedelta

from .models import Index, Coin, IndexPrice, IndexDay


def collect():
    coins = Coin.objects.all()
    indices = Index.objects.all()

    url1 = 'https://api.coincap.io/v2/assets?limit=1000'

    r1 = requests.get(url1)

    while r1.status_code != 200:
        sleep(10)
        r1 = requests.get(url1)

    data_1 = json.loads(r1.text)

    for coin in coins:

        entries = data_1['data']

        if coin.symbol == 'BCO':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2033/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'BTM':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/1866/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'PAI':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2900/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'NRG':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3218/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'BTCP':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2575/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'CRO':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3635/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'BTT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3718/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'IOT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/1720/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'CMT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2246/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'HOT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2682/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'COSS':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/1989/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'KCS':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2087/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'NEC':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2538/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'CNX':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2027/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'WGR':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/1779/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'PLAT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3633/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'PLAT':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3633/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'PLA':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3711/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'DGTX':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2772/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'R':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2135/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'MOAC':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2403/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])


        elif coin.symbol == 'SWTH':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2620/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'TIOX':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/3642/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'WICC':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2346/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol == 'DTR':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2298/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data = json.loads(r2.text)

            coin.price = float(data['data']['quotes']['USD']['price'])
            coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        else:

            for i in range(len(entries)):

                 if coin.symbol == entries[i]['symbol']:

                    coin.price = float(entries[i]['priceUsd'])
                    coin.price_percent_change = '{0:.2f}'.format(float(entries[i]['changePercent24Hr']))
                    coin.volume = '{0:.0f}'.format(float(entries[i]['volumeUsd24Hr']))
                    coin.market_cap = '{0:.0f}'.format(float(entries[i]['marketCapUsd']))
                    coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

    for dex in indices:

        if dex.name != 'Null':
            dex_coins = dex.coin_set.all()
            dex_market_cap = 0.0

            for dex_coin in dex_coins:
                dex_market_cap += float(dex_coin.market_cap)

            dex_price = float(dex_market_cap) / float(dex.divisor)
            dex_percent_change = 0

            # if dex.name != 'Gaming':

            entries = dex.indexprice_set.order_by('-timestamp')
            latest_entry = entries[0]

            current_date = latest_entry.timestamp
            current_seconds = current_date.second
            currrent_microseconds = current_date.microsecond

            yesterday = current_date - timedelta(days=1, seconds=current_seconds, microseconds=currrent_microseconds)
            yesterday2 = yesterday + timedelta(minutes=1)

            for last in entries:
                last_24_time = last.timestamp
                last_seconds = last_24_time.second
                last_micro = last_24_time.microsecond
                day_change = 0
                strip_time = last_24_time - timedelta(seconds=last_seconds, microseconds=last_micro)

                if strip_time == yesterday2:
                    this_change = float(dex_price) - float(last.price)
                    dex_percent_change = float(this_change) / float(last.price) * 100
                    break
                elif int(latest_entry.id) - int(last.id) > 7000:
                    this_change = latest_entry.change_24h
                    dex_percent_change = latest_entry.price_percent_change
                    break

            # else:
            #     this_change = 0


            new_dex_history = IndexPrice(index=dex,
                                         price=dex_price,
                                         change_24h=this_change,
                                         # change_24h='0.0',
                                         price_percent_change=dex_percent_change,
                                         # price_percent_change='0.0',
                                         market_cap=dex_market_cap,
                                         divisor=dex.divisor
                                         )

            new_dex_history.save()

    sleep(60)


def clear_price():
    n = 1
    entries = IndexDay.objects.all()
    for entry in entries:
        print(entry.rsi_14)
    # print('Deleting...')
    # entries.delete()

    print('Done')


def day_data(index, hour):
    day = 0
    displayed_prices = []
    index = Index.objects.get(name=index)
    prices = index.indexprice_set.order_by('timestamp')
    new_prices = prices.filter(timestamp__hour=hour)

    #Finds and stores price from each day at 16:00 UTC, or averages difference if missing
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

    return displayed_prices


def rsi_calc():
    displayed_prices = day_data("AltDex100", 16)
    # day = 0
    # displayed_prices = []
    # index = Index.objects.get(name="AltDex100")
    # prices = index.indexprice_set.order_by('timestamp')
    # new_prices = prices.filter(timestamp__hour=16)
    #
    # #Finds and stores price from each day at 16:00 UTC, or averages difference if missing
    # for price in new_prices:
    #     this_day = price.timestamp.day
    #     day_diff = abs(this_day - day)
    #
    #     if day_diff == 2:
    #         missing_day = price.timestamp - timedelta(days=1)
    #         missing_price = price.price - price.change_24h
    #         s_info = {'date' :missing_day,
    #                   'price': missing_price}
    #
    #         displayed_prices.append(s_info)
    #
    #     if this_day != day:
    #         info = {'date': price.timestamp,
    #                 'price': price.price}
    #
    #         displayed_prices.append(info)
    #         day = this_day
    #
    gain = 0
    lose = 0
    avg_gain = 0
    avg_lose = 0
    rsi_values = []
    twelve_ema = []
    twentysix_ema = []
    times2 = []

    # 12 Day EMA
    # times = []
    # differences = []
    # ema_9 = []
    # period_26 = 26
    # period_12 = 12
    # multiplier_12 = float(2 / (period_12 + 1))
    # multiplier_26 = float(2 / (period_26 + 1))
    # multiplier_9 = float(2 / (9 + 1))
    # sum_26 = 0
    # sum_12 = 0
    # sma_macd = 0
    # sma_12 = 0
    # sma_26 = 0
    # sum_macd = 0

    #MACD Calculation
    # for j in range(len(displayed_prices)):
    #
    #     #Summing up prices for EMA Calculaions
    #     if j <= period_12:
    #         sum_12 += displayed_prices[j]['price']
    #         sum_26 += displayed_prices[j]['price']
    #         # test.append(sum)
    #
    #     #Starting EMA 12 Calculation, while continuing to sum for EMA 26
    #     elif j == (period_12 + 1):
    #         sma_12 = float(sum_12) / float(period_12)
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(sma_12)) * multiplier_12) + float(sma_12)
    #
    #         sum_26 += displayed_prices[j]['price']
    #
    #     elif (period_12 + 1) < j <= period_26:
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(ema_12)) * multiplier_12) + float(ema_12)
    #
    #         sum_26 += displayed_prices[j]['price']
    #
    #     #Starting EMA 26 Calculations and differences for MACD
    #     elif j == (period_26 + 1):
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(ema_12)) * multiplier_12) + float(ema_12)
    #
    #         sma_26 = float(sum_26) / float(period_26)
    #         ema_26 = ((float(displayed_prices[j]['price']) - float(sma_26)) * multiplier_26) + float(sma_26)
    #
    #         difference = ema_12 - ema_26
    #
    #         sum_macd += difference
    #
    #     elif (period_26 + 1) < j <= (period_26 + 9):
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(ema_12)) * multiplier_12) + float(ema_12)
    #
    #         ema_26 = ((float(displayed_prices[j]['price']) - float(ema_26)) * multiplier_26) + float(ema_26)
    #
    #         difference = ema_12 - ema_26
    #
    #         sum_macd += difference
    #
    #     #Starting EMA for MACD
    #     elif j == (period_26 + 10):
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(ema_12)) * multiplier_12) + float(ema_12)
    #
    #         ema_26 = ((float(displayed_prices[j]['price']) - float(ema_26)) * multiplier_26) + float(ema_26)
    #
    #         difference = ema_12 - ema_26
    #
    #         sma_macd = float(sum_macd) / float(9)
    #
    #         ema_macd = ((float(difference) - float(sma_macd)) * multiplier_9) + float(sma_macd)
    #
    #         times.append(displayed_prices[j]['date'])
    #         differences.append(difference)
    #         ema_9.append(ema_macd)
    #
    #     else:
    #         ema_12 = ((float(displayed_prices[j]['price']) - float(ema_12)) * multiplier_12) + float(ema_12)
    #
    #         ema_26 = ((float(displayed_prices[j]['price']) - float(ema_26)) * multiplier_26) + float(ema_26)
    #
    #         difference = ema_12 - ema_26
    #
    #         ema_macd = ((float(difference) - float(ema_macd)) * multiplier_9) + float(ema_macd)
    #
    #         # test.append(ema_12)
    #         # test.append(ema_26)
    #         times.append(displayed_prices[j]['date'])
    #         differences.append(difference)
    #         ema_9.append(ema_macd)


    # RSI Calculation
    for i in range(1, len(displayed_prices)):
        this_price_change = displayed_prices[i]['price'] - displayed_prices[i-1]['price']

        rs_value = 0
        rsi_value = 0

        if i < 14:
            if this_price_change >= 0:
                gain += this_price_change
            else:
                lose += abs(this_price_change)

        elif i == 14:

            if this_price_change >= 0:
                gain += this_price_change
            else:
                lose += abs(this_price_change)

            avg_gain = float(gain) / 14
            avg_lose = float(lose) / 14

            rs_value = float(avg_gain) / float(avg_lose)
            rsi_value = 100 - (100 / (1 + float(rs_value)))

            rsi_values.append(rsi_value)
            times2.append(displayed_prices[i]['date'])

        else:
            this_gain = 0
            this_lose = 0

            if this_price_change >= 0:
                this_gain = this_price_change

            else:
                this_lose = abs(this_price_change)


            avg_gain = ((float(avg_gain) * (13)) + float(this_gain)) / 14
            avg_lose = ((float(avg_lose) * (13)) + float(this_lose)) / 14


            rs_value = float(avg_gain) / float(avg_lose)

            rsi_value = 100 - (100 / (1 + float(rs_value)))

            rsi_values.append(rsi_value)
            times2.append(displayed_prices[i]['date'])

    test = []

    #Saving to JSON dictionary for plotly.js
    # trace1 = {'x': times, 'y': differences, 'type': 'scatter', 'yaxis': 'y2',  'mode': 'lines', 'name': 'MACD'}
    # trace2 = {'x': times, 'y': ema_9, 'type': 'scatter', 'yaxis': 'y2',  'mode': 'lines', 'name': 'Signal Line'}
    trace3 = {'x': times2, 'y': rsi_values, 'type': 'scatter', 'yaxis': 'y2', 'mode': 'lines', 'name': 'RSI'}

    # test.append(trace1)
    # test.append(trace2)
    test.append(trace3)

    print(test)

    return
    # JsonResponse({'prices': test})


def first_weight():
    index = Index.objects.filter(name='Gaming')

    cap = 0
    divisor = 0
    # price = index.indexprice_set.last()
    coins = index.coin_set.all()

    for coin in coins:
        cap += coin.market_cap

    divisor = cap/100

    setattr(index, 'divisor', divisor)
    new_price = IndexPrice(index=index,
                           price=100,
                           change_24h=0,
                           price_percent_change=0,
                           market_cap=cap,
                           divisor=divisor
                           )
