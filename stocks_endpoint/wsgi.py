"""
WSGI config for stocks_endpoint project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stocks_endpoint.settings')
application = get_wsgi_application()

RULES = {}

def add_rule(rule, function):
    RULES[rule] = function

def get_rule(rule):
    try:
        return RULES[rule]

    except :
        print(str(rule)+ " not found")
        return None

def get_all_rules():
    return RULES