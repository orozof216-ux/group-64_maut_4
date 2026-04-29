from django.urls import path
from .import views

urlpatterns = [
    path('message/', views.mass, name='massage'),
    path('emoji/', views.emodji, name='emoji'),
    
]