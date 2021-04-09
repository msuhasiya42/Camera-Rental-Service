
from django.shortcuts import redirect


def logout(request):
    print(request.session.get('username'))
    request.session.clear()
    print(request.session.get('username'))

    return redirect('login')
