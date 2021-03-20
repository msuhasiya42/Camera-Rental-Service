from django.urls import path

from .import views

    #Blank for home page
urlpatterns = [


    path('login/',views.login, name='Login'),
    path('regis/',views.regis,  name='Register'),
    path('',views.home, name='Home')
]