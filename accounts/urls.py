from django.urls import path

from .import views

    #Blank for home page
urlpatterns = [
    path('accountHome/',views.accountHome, name= 'Home'),
]