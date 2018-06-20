from django.apps import AppConfig


class AltdexConfig(AppConfig):
    name = 'altdex'


SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True