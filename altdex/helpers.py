import requests
import json
from time import sleep

from .models import Index, Coin, IndexPrice


def collect():
    # print('called')
    coins = Coin.objects.all()
    indices = Index.objects.order_by('name')

    # print(0)

    url = 'http://coincap.io/front'
    r = requests.get(url)
    data = json.loads(r.text)

    for coin in coins:

        for i in range(len(data) - 1):
            entry = data[i]

            if entry['short'] == coin.symbol:
                coin.price = float(entry['price'])
                coin.price_percent_change = float('{0:.2f}'.format(entry['perc']))
                coin.volume = float('{0:.0f}'.format(entry['usdVolume']))
                coin.market_cap = float('{0:.0f}'.format(entry['mktcap']))
                coin.percent_weight = 0

                coin.save(update_fields=['price', 'price_percent_change', 'volume', 'market_cap', 'percent_weight'])


    for dex in indices:
        dex_coins = dex.coin_set.all()
        dex_market_cap = 0.0

        # for i in range(len(coin_table)):
        for dex_coin in dex_coins:
            dex_market_cap += float(dex_coin.market_cap)

        dex_price = float(dex_market_cap) / float(dex.divisor)
        dex_percent_change = 0
        amount_entries = len(dex.indexprice_set.all())
        last_id = dex.indexprice_set.last().id

        if amount_entries < 2189:
            this_change = 0
        else:
            price_id = last_id - 2189
            last_price = dex.indexprice_set.get(id=price_id).price
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

        # print(coin_table)
    # return coin_table


    sleep(30)




