from django.urls import path
from . import views

urlpatterns = [
    path('quote1/', views.quote1, name='quote1'),
    path('quote2/', views.quote2, name='quote2'),
    path('quote3/', views.quote3, name='quote3'),
]