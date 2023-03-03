from django.urls import path
from . import views

from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name="home"),
    path('download', views.download, name="done"),
    path('extended', views.extended, name="extended"),
    path('vue', TemplateView.as_view(template_name = 'index.html')),
    ]