from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('general/', views.contactgeneral, name='contact general'),
    
    
]