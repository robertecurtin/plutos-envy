from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^unit/(?P<unit_name_slug>[\w\-]+)/$', views.unit, name='unit'),   
        url(r'^city/(?P<city_name_slug>[\w\-]+)/$', views.city, name='city'),   
        url(r'^player/(?P<player_name_slug>[\w\-]+)/$', views.player, name='player'),   
        url(r'^orders/(?P<unit_name_slug>[\w\-]+)/$', views.orders, name='orders'),   
        url(r'^simulateday/$', views.simulate_day_callback),   
        url(r'^gamelog/$', views.view_game_log),
        ]
