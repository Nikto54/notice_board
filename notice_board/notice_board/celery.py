import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'notice_board.settings')

app = Celery('notice_board')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()