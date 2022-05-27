import os
from django.contrib import admin
from django.urls import path, include, re_path
from oauth2_provider.views import ConnectDiscoveryInfoView

base_path = os.environ.get('URL_BASE_PATH', '').strip('/')
trailing_slash = ''
if base_path:
    trailing_slash = '/'

urlpatterns = [
    path(f'''{base_path}{trailing_slash}admin/''', admin.site.urls),
    path(f'''{base_path}{trailing_slash}''', include('des_oauth.urls')),
    path(f'''{base_path}{trailing_slash}accounts/''', include('django.contrib.auth.urls')),
    ## Some OIDC clients do not follow redirects supplied by the APPEND_SLASH option
    ## ref: https://github.com/jazzband/django-oauth-toolkit/issues/1089#issuecomment-1038442830
    re_path(f'^{base_path}{trailing_slash}oidc/\.well-known/openid-configuration/?$',
            ConnectDiscoveryInfoView.as_view(), name='oidc-connect-discovery-info'),
    path(f'''{base_path}{trailing_slash}oidc/''',
         include('oauth2_provider.urls', namespace='oauth2_provider')),
]  # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
