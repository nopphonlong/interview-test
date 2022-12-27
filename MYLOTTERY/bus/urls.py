from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


busrouter = routers.DefaultRouter()
busrouter.register(r'cartypes', views.CartypeViewSet)
busrouter.register(r'buses', views.BusViewSet)
busrouter.register(r'owners', views.OwnerViewSet)
busrouter.register(r'tickets', views.TicketViewSet)
busrouter.register(r'seats', views.SeatView)
busrouter.register(r'seat_reserve', views.SeatReserve)
busrouter.register(r'seat_buy', views.SeateBuy)




urlpatterns = [
    path('', include(busrouter.urls)),
]