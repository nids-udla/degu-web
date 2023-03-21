from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('team', views.team, name='team'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
    path('filter', views.filter, name='filter'),
    path('download', views.download, name="download"),
    path('extended', views.extended, name="extended"),
    ]