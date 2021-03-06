from django.urls import path
from . import views

app_name = 'altdex'

urlpatterns = [
    path('', views.altdex, name='altdex'),
    path('alt100/', views.alt100, name='alt100'),
    path('exchange/', views.exchange, name='exchange'),
    path('privacy/', views.privacy, name='privacy'),
    path('masternode/', views.masternode, name='masternode'),
    path('gaming/', views.gaming, name='gaming'),
    path('news/', views.news, name='news'),
    path('pullcurrent/', views.pullcurrent, name='pullcurrent'),
    path('getindexcurrent/', views.getindexcurrent, name='getindexcurrent'),
    path('getindexall/', views.getindexall, name='getindexall'),
    path('getmasterindex/', views.getmasterindex, name='getmasterindex'),
    path('getmainindex/', views.getmainindex, name='getmainindex'),
    path('getexchangeindex/', views.getexchangeindex, name='getexchangeindex'),
    path('getprivacyindex/', views.getprivacyindex, name='getprivacyindex'),
    path('getgamingindex/', views.getgamingindex, name='getgamingindex'),
    path('getcoinscurrent/', views.getcoinscurrent, name='getcoinscurrent'),
    path('getindexperformance/', views.getindexperformance, name='getindexperformance'),
    path('rsi_calc/', views.rsi_calc, name='rsi_calc'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('gainers_losers/', views.gainers_losers, name='gainers_losers'),
    path('about/', views.about, name='about'),
    path('testing/', views.testing, name='testing'),
    path('testing2/', views.testing2, name='testing2'),
    path('index_trend/', views.index_trend, name='index_trend'),
    path('exchange_trend/', views.exchange_trend, name='exchange_trend'),
    path('privacy_trend/', views.privacy_trend, name='privacy_trend'),
    path('master_trend/', views.master_trend, name='master_trend'),
    path('gaming_trend/', views.gaming_trend, name='gaming_trend'),
    path('main_trend/', views.main_trend, name='main_trend'),
    path('trend_test/', views.trend_test, name='trend_test'),
]
