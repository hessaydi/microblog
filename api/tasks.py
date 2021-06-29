from __future__ import absolute_import, unicode_literals

# from celery import shared_task
from datetime import  timedelta
from celery.decorators import task
from celery.utils.log import get_task_logger
from api import models
from .email import send_email, send_notification_email
from django.utils import timezone
logger = get_task_logger(__name__)

@task(name="send_email_task")
def send_email_task(username, email):
    logger.info("Sent registration email")
    return send_email(username, email)


# @shared_task
@task(name="delete_messages_in_ten_days")
def delete_messages_in_ten_days():
    logger.info("Deleteed Posts")
    models.Post.objects.filter(created_at__lte=timezone.now()-timedelta(days=10)).delete()
    return "Delete posts create over then 10 days"

# celery -A core beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
@task(name='send_a_notification_email')
def send_a_notification_email(username, email, hashtag):
    logger.info("Sent a notification email")
    return send_notification_email(username, email, hashtag)
