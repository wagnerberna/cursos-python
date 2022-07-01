"""
WSGI config for tourist_spot project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tourist_spot.settings")

# padrão
# application = get_wsgi_application()

# p/ heroku
# cada req. q chega verifica se é um arq. estático, senão envia p/ django
application = Cling(get_wsgi_application())
