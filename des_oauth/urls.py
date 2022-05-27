from multiprocessing import context
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
import os

base_path = os.environ.get('URL_BASE_PATH', '').strip('/')
trailing_slash = ''
if base_path:
    trailing_slash = '/'

urlpatterns = [
    path(f'''''', views.index, name='index'),
    path(f'''accounts/login/''', auth_views.LoginView.as_view(
        template_name='des_oauth/login.html',
        extra_context={'password_reset_link': 'https://deslabs.ncsa.illinois.edu/desaccess/login'})
    ),
    path(f'''accounts/profile/''', views.profile),
]
