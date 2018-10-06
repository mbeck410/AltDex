import requests
import json
from time import sleep
from datetime import timedelta

from .models import Index, Coin, IndexPrice


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

        if coin.symbol == 'COB':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2006/'
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

        elif coin.symbol == 'DROP':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2591/'
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

        elif coin.symbol == 'HC':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/1903/'
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

            new_dex_history = IndexPrice(index=dex,
                                         price=dex_price,
                                         change_24h=this_change,
                                         price_percent_change=dex_percent_change,
                                         market_cap=dex_market_cap,
                                         divisor=dex.divisor
                                         )

            new_dex_history.save()

    sleep(60)


def clear_price():
    n = 1
    entries = IndexPrice.objects.all()
    print('Deleting...')
    entries.delete()

    print('Done')


def first_weight():
    index = Index.objects.filter(name='Masternode')

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
