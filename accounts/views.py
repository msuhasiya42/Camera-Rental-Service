from django.shortcuts import render

# Create your views here.

def accountHome(request):
    return render(request, 'home.html')