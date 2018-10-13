from django.contrib import admin
from .models import Index, Coin, IndexPrice, IndexDay, Test

admin.site.register(Index)
admin.site.register(IndexPrice)
admin.site.register(Coin)
admin.site.register(IndexDay)
admin.site.register(Test)
