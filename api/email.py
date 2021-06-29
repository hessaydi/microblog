
from django.template import Context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings


def send_email(username, email):
    context = {
        'username': username,
        'email': email,
    }
    email_subject = 'Registration email'
    email_body = render_to_string('email_message.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)

def send_notification_email(username, email, hashtag):
    context = {
        'username': username,
        'email': email,
        'hashtag': hashtag,
    }
    email_subject = 'Notification email'
    email_body = render_to_string('notification_email.txt', context)

    email = EmailMessage(
        email_subject, email_body,
        settings.DEFAULT_FROM_EMAIL, [email, ],
    )
    return email.send(fail_silently=False)