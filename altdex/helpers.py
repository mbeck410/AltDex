import requests
import json
from time import sleep

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
        sleep(30)
        r1 = requests.get(url1)

    data_1 = json.loads(r1.text)
    # data_2 = json.loads(r2.text)
    # data_3 = json.loads(r3.text)

    for coin in coins:

        # if coin.symbol in symbols:
        #     coin.price = float(data_2['RAW'][coin.symbol]['USD']['PRICE'])
        #     coin.price_percent_change = '{0:.2f}'.format(float(data_2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
        #     coin.volume = '{0:.0f}'.format(float(data_2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
        #     coin.market_cap = '{0:.0f}'.format(float(data_2['RAW'][coin.symbol]['USD']['MKTCAP']))
        #     coin.percent_weight = 0
        #
        #     coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])
        #
        # elif coin.symbol in symbols2:
        #     coin.price = float(data_3['RAW'][coin.symbol]['USD']['PRICE'])
        #     coin.price_percent_change = '{0:.2f}'.format(float(data_3['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
        #     coin.volume = '{0:.0f}'.format(float(data_3['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
        #     coin.market_cap = '{0:.0f}'.format(float(data_3['RAW'][coin.symbol]['USD']['MKTCAP']))
        #     coin.percent_weight = 0
        #
        #     coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        for i in range(len(data_1) - 1):
            entry = data_1[i]

            if entry['short'] == coin.symbol:

                coin.price = float(entry['price'])
                coin.price_percent_change = '{0:.2f}'.format(float(entry['perc']))
                coin.volume = '{0:.0f}'.format(float(entry['usdVolume']))
                coin.market_cap = '{0:.0f}'.format(float(entry['mktcap']))
                coin.percent_weight = 0

                if entry['short'] == 'CMT':
                    url2 = 'https://api.coinmarketcap.com/v2/ticker/' + str(coin.coin_marketcap_id)
                    r2 = requests.get(url2)

                    while r2.status_code != 200:
                        sleep(30)
                        r2 = requests.get(url2)

                    data = json.loads(r2.text)

                    coin.price = float(data['data']['quotes']['USD']['price'])
                    coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
                    coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
                    coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
                    coin.percent_weight = 0

                coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

    for dex in indices:
        if str(dex.name) is not 'Null':
            dex_coins = dex.coin_set.all()
            dex_market_cap = 0.0

            # for i in range(len(coin_table)):
            for dex_coin in dex_coins:
                dex_market_cap += float(dex_coin.market_cap)

            dex_price = float(dex_market_cap) / float(dex.divisor)
            dex_percent_change = 0
            amount_entries = len(dex.indexprice_set.all())

            if amount_entries < 1351:
                this_change = 0

            else:
                price_id = amount_entries - 1182
                last_price = dex.indexprice_set.all()[price_id].price
                this_change = float(dex_price) - float(last_price)
                dex_percent_change = (this_change/float(last_price)) * 100

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
    indices = Index.objects.all()

    for index in indices:
        divisor = 0
        price = index.indexprice_set.last()
        coins = index.coin_set.all()

        for coin in coins:
            divisor += coin.market_cap

        divisor /= 100

        setattr(index, 'divisor', divisor)
        setattr(price, 'price', 100)






