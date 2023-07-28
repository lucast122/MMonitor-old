"""
WSGI config for MMonitor project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application

#from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MMonitor.settings')

#module= wsgi:application
application = get_wsgi_application()
#from index import server as application
#if __name__ == '__main__':
#    application = get_wsgi_application()
