from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Башкы бет үчүн
    path('contact/', views.contact, name='contact'),  # Байланыш формасы үчүн
]
