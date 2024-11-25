from django.urls import path
from . import views

urlpatterns = [
    path('', views.counter, name='counter'),
    path('counter/', views.counter, name='counter'),
]