from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('login/', views.LoginAPIView.as_view(), name='login'),
    # path('oauth2/token/', views.TokenAPIView.as_view(), name='token'),
    path('refresh-token/', views.RefreshTokenView.as_view(), name='refresh_token'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('', include(router.urls)),
]