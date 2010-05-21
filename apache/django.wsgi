import os
import sys

sys.path.append('/home/refik/sandbox')
sys.path.append('/home/refik/sandbox/ava')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ava.settings'
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
