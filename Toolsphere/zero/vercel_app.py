import os
import sys

# Add the project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'zero.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create the WSGI application
application = get_wsgi_application()

# Vercel expects 'app' variable
app = application