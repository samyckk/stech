import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyWeb.settings')

# Define the handler for Vercel
handler = get_wsgi_application()


# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyWeb.settings')

# application = get_wsgi_application()
