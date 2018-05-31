import requests
import json
from time import sleep

from .models import Index, Coin, IndexPrice


def collect():
    # print('called')
    coins_cc = Coin.objects.filter(api='CryptoCompare')
    coins_cmc = Coin.objects.filter(api='CMC')
    indices = Index.objects.order_by('name')
    symbols = []
    symbols2 = []
    # print(0)



    for coin in coins_cc:
        if len(symbols) < 50:
            symbols.append(coin.symbol)
        else:
            symbols2.append(coin.symbol)

    sym_str1 = ','.join(symbols)
    sym_str2 = ','.join(symbols2)

    # print(symbols)

    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + sym_str1 + '&tsyms=USD'
    url2 = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + sym_str2 + '&tsyms=USD'
    r = requests.get(url)
    r2 = requests.get(url2)
    data = json.loads(r.text)
    data2 = json.loads(r2.text)

    # print('1')

    # coin_table = []
    # coin_histories = {}

    for coin in coins_cc:
        dices = ''
        indices_in = coin.indices.all()

        for dex in indices_in:
            dices += str(dex.name)

        # if coin.symbol is 'R':
        #     if 'R' in symbols:
        #         coin.price = float(data['RAW'][coin.symbol]['USD']['PRICE'])
        #         coin.price_percent_change = float('{0:.2f}'.format(data['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
        #         coin.volume = float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
        #         coin.market_cap = float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['MKTCAP']))
        #         coin.percent_weight = 0
        #
        #     else:
        #         coin.price = float(data2['RAW'][coin.symbol]['USD']['PRICE'])
        #         coin.price_percent_change = float('{0:.2f}'.format(data2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
        #         coin.volume = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
        #         coin.market_cap = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['MKTCAP']))
        #         coin.percent_weight = 0
        #
        #     coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        if coin.symbol in symbols:
            coin.price = float(data['RAW'][coin.symbol]['USD']['PRICE'])
            coin.price_percent_change = float('{0:.2f}'.format(data['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
            coin.volume = float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
            coin.market_cap = float('{0:.0f}'.format(data['RAW'][coin.symbol]['USD']['MKTCAP']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        else:
            # new_coin_history = {'coin': coin.name,
            #                     'symbol': coin.symbol,
            #                     'price': '{0:.2f}'.format(float(data2['RAW'][coin.symbol]['USD']['PRICE'])),
            #                     'price_percent_change': float(
            #                         '{0:.2f}'.format(data2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR'])),
            #                     'volume': float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H'])),
            #                     'market_cap': float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['MKTCAP'])),
            #                     'indices': dices,
            #                     'percent_weight': 0
            #                     }

            coin.price = float(data2['RAW'][coin.symbol]['USD']['PRICE'])
            coin.price_percent_change = float('{0:.2f}'.format(data2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
            coin.volume = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
            coin.market_cap = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['MKTCAP']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        # dict_entry = {coin.name: new_coin_history}

        # coin_histories.update(dict_entry)

        # coin_table.append(new_coin_history)

    # print('2')

    for coin in coins_cmc:
        url = 'https://api.coinmarketcap.com/v2/ticker/' + str(coin.coin_marketcap_id)
        r = requests.get(url)
        data = json.loads(r.text)

        dices = ''
        indices_in = coin.indices.all()

        for dex in indices_in:
            dices += str(dex.name)

        # print(dices)

        coin.price = float(data['data']['quotes']['USD']['price'])
        coin.price_percent_change = float('{0:.2f}'.format(data['data']['quotes']['USD']['percent_change_24h']))
        coin.volume = float('{0:.0f}'.format(data['data']['quotes']['USD']['volume_24h']))
        coin.market_cap = float('{0:.0f}'.format(data['data']['quotes']['USD']['market_cap']))
        coin.percent_weight = 0

        coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        # dict_entry = {coin.name: new_coin_history}

        # coin_histories.update(dict_entry)

        # coin_table.append(new_coin_history)

    for dex in indices:
        dex_coins = dex.coin_set.all()
        dex_market_cap = 0.0

        # for i in range(len(coin_table)):
        for dex_coin in dex_coins:
            dex_market_cap += float(dex_coin.market_cap)

        dex_price = float(dex_market_cap) / float(dex.divisor)
        dex_percent_change = 0
        length = len(dex.indexprice_set.all())
        print(length)
        print(dex.indexprice_set.last().id)

        if length < 2189:
            this_change = 0
        else:
            price_id = length - 2189
            price_obj = dex.indexprice_set.filter(id=price_id)

            last_price = price_obj.price
            this_change = dex_price - last_price




        new_dex_history = IndexPrice(index=dex,
                                     price=dex_price,
                                     change_24h=this_change,
                                     price_percent_change=dex_percent_change,
                                     market_cap=dex_market_cap,
                                     divisor=dex.divisor
                                     )

        new_dex_history.save()

        # print(coin_table)
    # return coin_table

    sleep(30)




