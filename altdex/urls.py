from django.urls import path
from . import views

app_name = 'altdex'

urlpatterns = [
    path('', views.altdex, name='altdex'),
    path('exchange/', views.exchange, name='exchange'),
    path('privacy/', views.privacy, name='privacy'),
    path('masternode/', views.masternode, name='masternode'),
    path('pullcurrent/', views.pullcurrent, name='pullcurrent'),
    path('getindexcurrent/', views.getindexcurrent, name='getindexcurrent'),
    path('getindexall/', views.getindexall, name='getindexall'),
    path('getcoinscurrent/', views.getcoinscurrent, name='getcoinscurrent'),
    path('index_data/', views.index_data, name='index_data'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('gainers_losers/', views.gainers_losers, name='gainers_losers'),
    path('about/', views.about, name='about'),
    path('testing/', views.testing, name='testing'),
]
