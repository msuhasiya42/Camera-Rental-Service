

from django.shortcuts import render, redirect


def logout(request):
    request.session.clear()
    return redirect('login')
