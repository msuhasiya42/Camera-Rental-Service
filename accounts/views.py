from django.shortcuts import render

# Create your views here.

def loginreg(request):
    return render(request, 'home.html')