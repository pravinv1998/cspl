from django.http import HttpResponse,Http404
from django.shortcuts import redirect
from django.shortcuts import render

def allowed_users(allowed_role=[]):
    def decorator(view_func):
        def wraper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_role:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('Unauthorised access, Login using authorised credentional!!!')          
        return wraper_func
    return decorator
