from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from users.views import login_view as login, create_view, logout_view

urlpatterns = [
    path('login/',login,name='login_view'),
    path('cadastro/',create_view,name='cadastro_view'),
    path('logout/',logout_view,name='logout_view'),
]