"""
WSGI config for rent-a-car project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# Ajusta el nombre del módulo de configuración según el nombre de tu proyecto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rent_a_car.settings')

application = get_wsgi_application()
