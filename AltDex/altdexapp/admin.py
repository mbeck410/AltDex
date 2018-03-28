from django.contrib import admin
from .models import Index, Coin, IndexCurrent, CoinCurrent, IndexDay, CoinDay

admin.site.register(Index)
admin.site.register(IndexCurrent)
admin.site.register(IndexDay)
admin.site.register(Coin)
admin.site.register(CoinCurrent)
admin.site.register(CoinDay)

