import requests
import json

from .models import Index, Coin, IndexPrice


def collect():
    print('!!!')
    coins_cc = Coin.objects.filter(api='CryptoCompare')
    coins_cmc = Coin.objects.filter(api='CMC')
    indices = Index.objects.order_by('name')
    symbols = ''
    symbols2 = ''

    for coin in coins_cc:
        if len(symbols) < 250:
            symbols += coin.symbol + ','
        else:
            symbols2 += coin.symbol + ','

    symbols = symbols[:-1]
    symbols2 = symbols2[:-1]

    url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols + '&tsyms=USD'
    url2 = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms=' + symbols2 + '&tsyms=USD'
    r = requests.get(url)
    r2 = requests.get(url2)
    data = json.loads(r.text)
    data2 = json.loads(r2.text)

    # coin_table = []
    # coin_histories = {}

    for coin in coins_cc:
        dices = ''
        indices_in = coin.indices.all()

        for dex in indices_in:
            dices += str(dex.name)

        # print(symbols)

        if coin.symbol is 'R':
            coin.price = '{0:.2f}'.format(float(data2['RAW'][coin.symbol]['USD']['PRICE']))
            coin.price_percent_change = float('{0:.2f}'.format(data2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
            coin.volume = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
            coin.market_cap = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['MKTCAP']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        elif coin.symbol in symbols:
            coin.price = '{0:.2f}'.format(float(data['RAW'][coin.symbol]['USD']['PRICE']))
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

            coin.price = '{0:.2f}'.format(float(data2['RAW'][coin.symbol]['USD']['PRICE']))
            coin.price_percent_change = float('{0:.2f}'.format(data2['RAW'][coin.symbol]['USD']['CHANGEPCT24HOUR']))
            coin.volume = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['TOTALVOLUME24H']))
            coin.market_cap = float('{0:.0f}'.format(data2['RAW'][coin.symbol]['USD']['MKTCAP']))
            coin.percent_weight = 0

            coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])

        # dict_entry = {coin.name: new_coin_history}

        # coin_histories.update(dict_entry)

        # coin_table.append(new_coin_history)

    for coin in coins_cmc:
        url = 'https://api.coinmarketcap.com/v2/ticker/' + str(coin.coin_marketcap_id)
        r = requests.get(url)
        data = json.loads(r.text)

        dices = ''
        indices_in = coin.indices.all()

        for dex in indices_in:
            dices += str(dex.name)

        # print(dices)

        coin.price = float('{0:.2f}'.format(data['data']['quotes']['USD']['price']))
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
        length = len(IndexPrice.objects.all())

        if length < 2880:
            this_change = 0
        else:
            last_price = IndexPrice.objects.value(id=length-2880)
            this_change = dex_price - last_price




        new_dex_history = IndexPrice(index=dex,
                                     price=dex_price,
                                     change_24h=this_change,
                                     price_percent_change=dex_percent_change,
                                     market_cap=dex_market_cap,
                                     divisor=dex.divisor
                                     )

        new_dex_history.save()

        for dex_coin in dex_coins:
            dex_coin.percent_weight = '{0:.3f}'.format(float(dex_coin.market_cap) / float(dex_market_cap) * 100)
            dex_coin.save(update_fields=['percent_weight'])

        # print(coin_table)
    # return coin_table
