"""
WSGI config for dantorial project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import dotenv
dotenv.load_dotenv()

from django.core.wsgi import get_wsgi_application

dotenv.load_dotenv(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', os.getenv("DJANGO_SETTINGS_MODULE"))

if os.getenv('DJANGO_SETTINGS_MODULE'):
    os.environ['DJANGO_SETTINGS_MODULE'] = os.getenv('DJANGO_SETTINGS_MODULE')

application = get_wsgi_application()
<<<<<<< HEAD
app = application
=======
app = application
>>>>>>> 4f236226881f5ca1e6b8b1d3c212ad56d3e96d0b
