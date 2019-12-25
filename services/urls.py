from django.urls import path
from . import views

urlpatterns = [
    #Paths core
    path('', views.services, name="services")
]