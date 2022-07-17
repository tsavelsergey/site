from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('info/', views.info, name='info'),
    path('social/', views.social, name='social'),
    path('description/', views.description, name='description'),
]