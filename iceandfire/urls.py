from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('character/', views.get_character, name='get_character'),
    path('house/', views.get_house, name='get_house'),
    path('book/', views.get_book, name='get_book'),
]