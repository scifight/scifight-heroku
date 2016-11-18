import os
import sys
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

# Make project directory available for imports.
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "project"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scifight_heroku_settings")
application = DjangoWhiteNoise(get_wsgi_application())
