from django.urls import path
from . import views

app_name = 'online_store'

urlpatterns = [
    path('', views.home, name='home'),
    path('contacts', views.contacts, name='contacts'),
    path('categories', views.categories, name='categories'),
    path('orders', views.orders, name='orders'),
    path('pattern', views.pattern, name='pattern'),
    path('index', views.index, name='index'),
]