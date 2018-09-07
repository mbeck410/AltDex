import requests
import json
from time import sleep
from datetime import timedelta

from .models import Index, Coin, IndexPrice


def collect():
    coins = Coin.objects.all()
    indices = Index.objects.all()
    # coins_cc = Coin.objects.filter(api='CryptoCompare')
    # symbols = []
    # symbols2 = []
    #
    # for coin in coins_cc:
    #     if len(symbols) < 40:
    #         symbols.append(coin.symbol)
    #     else:
    #         symbols2.append(coin.symbol)
    #
    # sym_str1 = ','.join(symbols)
    # sym_str2 = ','.join(symbols2)

    url1 = 'http://coincap.io/front'
    # url2 = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + sym_str1 + '&tsyms=USD'
    # url3 = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + sym_str2 + '&tsyms=USD'

    r1 = requests.get(url1)

    while r1.status_code != 200:
        sleep(10)
        r1 = requests.get(url1)

    data_1 = json.loads(r1.text)
    # data_2 = json.loads(r2.text)
    # data_3 = json.loads(r3.text)

    for coin in coins:

        if coin.name == 'Pundi X':
            url2 = 'https://api.coinmarketcap.com/v2/ticker/2603/'
            r2 = requests.get(url2)

            while r2.status_code != 200:
                sleep(10)
                r2 = requests.get(url2)

            data_2 = json.loads(r2.text)

            coin.price = float(data_2['data']['quotes']['USD']['price'])
            coin.price_percent_change = '{0:.2f}'.format(float(data_2['data']['quotes']['USD']['percent_change_24h']))
            coin.volume = '{0:.0f}'.format(float(data_2['data']['quotes']['USD']['volume_24h']))
            coin.market_cap = '{0:.0f}'.format(float(data_2['data']['quotes']['USD']['market_cap']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])
        #
        # elif coin.symbol in symbols2:
        #     coin.price = float(data_3['RAW'][coin.symbol]['USD']['PRICE'])
        #     coin.price_percent_change = '{0:.2f}'.format(float(data_3['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
        #     coin.volume = '{0:.0f}'.format(float(data_3['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
        #     coin.market_cap = '{0:.0f}'.format(float(data_3['RAW'][coin.symbol]['USD']['MKTCAP']))
        #     coin.percent_weight = 0
        #
        #     coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])
        else:
            for i in range(len(data_1) - 1):
                entry = data_1[i]
                if coin.symbol == '$PAC':
                    symbol = 'PAC'
                else:
                    symbol = coin.symbol

                if entry['short'] == symbol:

                    coin.price = float(entry['price'])
                    coin.price_percent_change = '{0:.2f}'.format(float(entry['perc']))
                    coin.volume = '{0:.0f}'.format(float(entry['usdVolume']))
                    coin.market_cap = '{0:.0f}'.format(float(entry['mktcap']))
                    coin.percent_weight = 0

                    if entry['short'] == 'CMT':
                        url2 = 'https://api.coinmarketcap.com/v2/ticker/' + str(coin.coin_marketcap_id)
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
                    dex_percent_change = (float(this_change) / float(last.price)) * 100
                    break
                elif ((latest_entry.id - last.id) % 4) > 1300:
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
