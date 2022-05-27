from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        'organization': 'DES',
        'login_link': settings.LOGIN_URL,
    }
    return render(request, 'des_oauth/index.html', context)

def profile(request):
    context = {}
    return render(request, 'des_oauth/profile.html', context)

