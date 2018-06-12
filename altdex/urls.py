from django.urls import path
from . import views

app_name = 'altdex'

urlpatterns = [
    path('', views.altdex, name='altdex'),
    path('exchange/', views.exchange, name='exchange'),
    path('privacy/', views.privacy, name='privacy'),
    path('pullcurrent/', views.pullcurrent, name='pullcurrent'),
    path('getindexcurrent/', views.getindexcurrent, name='getindexcurrent'),
    path('getindexall/', views.getindexall, name='getindexall'),
    path('getcoinscurrent/', views.getcoinscurrent, name='getcoinscurrent'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('about/', views.about, name='about')
]

