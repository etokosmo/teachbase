import os

import requests
from django.conf import settings
from django.core.cache import cache
from rest_framework.exceptions import AuthenticationFailed

GRANT_TYPE = 'client_credentials'
TEACHBASE_TOKEN = 'teachbase_token'


def auth(auth_uri: str = 'oauth/token') -> None:
    auth_url = os.path.join(settings.TEACHBASE_API, auth_uri)
    payload = {
        'client_id': settings.CLIENT_ID,
        'client_secret': settings.CLIENT_SECRET,
        'grant_type': GRANT_TYPE,
    }
    response = requests.post(auth_url, data=payload)
    response.raise_for_status()
    success_response = response.json()

    access_token = success_response.get('access_token')
    cache.set(
        TEACHBASE_TOKEN,
        access_token,
        success_response.get('expires_in'),
    )


def refresh_token(func):
    def check_token_exists(*args, **kwargs):
        if not cache.get(TEACHBASE_TOKEN):
            try:
                auth()
            except (
                    requests.exceptions.HTTPError,
                    requests.exceptions.ConnectionError
            ):
                raise AuthenticationFailed
        return func(*args, **kwargs)

    return check_token_exists


@refresh_token
def get_token():
    """Get token from cache"""
    token = cache.get(TEACHBASE_TOKEN)
    if not token:
        raise AuthenticationFailed
    return token
