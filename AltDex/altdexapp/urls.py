from django.urls import path
from . import views

app_name = 'altdexapp'

urlpatterns = [
    path('', views.pullcurrent, name='pullcurrent'),
    path('pulldaily', views.pulldaily, name='pulldaily')
]