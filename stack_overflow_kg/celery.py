import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stack_overflow_kg.settings')

app = Celery('stack_overflow_kg')
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
