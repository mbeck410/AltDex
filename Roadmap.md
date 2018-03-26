# AltDex

## Cryptocurrency Index

### Overview

The idea for Altdex building indices of cryptocurrencies for the largest projects currently in the crypto market. Some of the
categories will include privacy coins, exchange coins, and finance coins, as well as an index that will hold the top 50 coins
by market cap. The indices will be dynamic, with the options to add and remove coins from the indices as the market 
evolves. Indices will be capitalization-weighted, meaning they will be weighted by the market cap values of the coins, using the 
following formula:

```
Coin Weight = \frac{market cap}{\sum{market caps}}
```

Then the sum of the weights is found and then divided by a number called a divisor to make the index price an easy number to work with,
such as $100 or $1000. When updating the index after adding or removing a coin, or after a set amount of time to account for the changes in market caps,
the divisor is recalculated using the formula:

```
New Divisor = \frac{market value after}{market value before} * Old Divisor
```

As of now, there is not a comprehensive index for cryptocurrencies. Indices are a valuable for investors to track markets,
and as the crypto world continues to grow a place to find overall trends in different sectors will be become extremely useful.

### Functionality

The site itself will display a graph of the current price and the history up to that point, updating automatically every
at a set interval. Users will be able to switch between charts for the indices as well as individual coins, and can have 
the chart display price, volume, and market cap. Different time periods can be viewed as well, last day, last 3 days,
last week, last month, etc. When changing between index or information, a chart will be generated on the back-end using 
python depending on the inputs specified by the user and then sent to be displayed.

Underneath the price graph, a list of all the coins in the index shown with daily individual data such as current price, 
daily dollar change, % dollar change, daily high, daily low, and daily volume. Included in the
list for each coin will be links to the coins' websites.

### Data Model

Using Django, a model will be made for each coin that will store the name, symbol, and index, and coins will have a 
many to one relationship with a coin history model that will have current price, volume, market cap, daily open,
daily change, % daily change. These tables can be populated by pulling JSON data from the CoinAPI, and the non-daily 
data can be updated after a set time of 30 seconds, which is supported by the API. Monthly highs and lows could also be stored
or can be calculated. Another model for the indices themselves would be used, made up of the coins, name of the index,
divisor and will have a Many-To-One relationship with its own history model that stores current market cap of the index, 
price, volume, and the divisor which will be used to calculate the price. The price and volume will be found using the 
sums of the coins' price and index that we populate them with. The relationship between the Index and the Coin 
will be Many-to-Many, as an index will be composed of many coins and the coins can be part of multiple indices. 
Charts can be created in the view, using a python extension for data visualization.


Models
Coin: name, symbol, index, website.
Index: name, coins, divisor.
Coin History: foreign key coin, current price, volume traded, market cap, daily open, daily change, %daily change, timestamp. 
Index History: foreign key index, current price, volume, market cap, daily open, daily change, % daily change, timestamp.

### Schedule:
First Week: Get database up and running, getting the coins in and the indices made with the correct coins.
Make sure the API is pulling the correct information and the models are having the correct information stored in the correct 
position in the database.

Second Week: Make charts and all the data visualization that the user will see on the webpage. Use a framework, probably
Bootstrap.Make sure the list of coins for each index populate with the correct information and the charts load the correct 
time period, data type, etc. Getlinks to coin websites working.

Third Week: Have the app automatically pull data from the API and automatically populate the databases and make sure that the 
site updates at the same time.

