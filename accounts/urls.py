from django.urls import path

from .import views

    #Blank for home page
urlpatterns = [
    path('loginreg/',views.loginreg, name= 'loginRegis'),
]