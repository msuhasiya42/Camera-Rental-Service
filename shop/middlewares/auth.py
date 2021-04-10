from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print(request.session.get('username'))
        # to go bak to orders page
        return_url = request.META['PATH_INFO']

        if not request.session.get('username') or request.session.get('vendorname'):
            return redirect(f'/login/?return_url={return_url}')

        response = get_response(request)
        return response

    return middleware