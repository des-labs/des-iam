from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from oauth2_provider.oauth2_validators import OAuth2Validator
import cx_Oracle
import requests
import logging

logger = logging.getLogger(__name__)


class OracleBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            response = requests.post(
                url='https://deslabs.ncsa.illinois.edu/desaccess/api/login',
                data={
                    'username': username,
                    'password': password,
                    'database': 'dessci',
                }
            )
        except Exception as e:
            logger.error(f'''Login API request error for "{username}": {e}''')
            raise e
        try:
            ## If the user is authenticated they will receive an API token
            user_info = response.json()
            assert user_info['token']
            first_name = user_info['name']
            last_name = user_info['lastname']
            email = user_info['email']
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                ## Create a new user
                user = User(username=username, first_name=first_name,
                            last_name=last_name, email=email)
                user.is_staff = False
                user.is_superuser = False
                user.save()
            return user
        except Exception as e:
            logger.info(
                f'''Authentication failed for username "{username}": {e}''')
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class CustomOAuth2Validator(OAuth2Validator):
    oidc_claim_scope = None

    def get_additional_claims(self, request):
        groups = []
        for group in request.user.groups.all():
            groups.append(group.name)
        if request.user.is_superuser:
            groups.append('django-admin')
        return {
            "given_name": request.user.first_name,
            "family_name": request.user.last_name,
            "name": ' '.join([request.user.first_name, request.user.last_name]),
            "preferred_username": request.user.username,
            "email": request.user.email,
            "groups": groups,
            "roles": groups,
        }
