from django.urls import path
from . import views

app_name = 'altdex'

urlpatterns = [
    path('', views.index, name='index'),
    path('pullcurrent/', views.pullcurrent, name='pullcurrent'),
    path('getindexcurrent/', views.getindexcurrent, name='getindexcurrent'),
    path('getindexall/', views.getindexall, name='getindexall'),
    path('getcoinscurrent/', views.getcoinscurrent, name='getcoinscurrent')
]

