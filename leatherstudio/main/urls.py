from django.urls import path
from . import views


urlpatterns = [
    path('main', views.index),
    path('catalog', views.catalog),
]
