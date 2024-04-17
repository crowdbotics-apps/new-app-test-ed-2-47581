"""
WSGI config for new_app_test_ed_2_47581 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "new_app_test_ed_2_47581.settings"
)

application = get_wsgi_application()
