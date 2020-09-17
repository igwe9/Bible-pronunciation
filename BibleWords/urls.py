from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.search, name='add'),
    path('search/', views.search, name='search'),
    path('list/', views.word_list, name='word_list'),
]

