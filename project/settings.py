import django_heroku
from .local_settings import *

django_heroku.settings(locals())
