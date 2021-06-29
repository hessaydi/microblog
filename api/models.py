from django.db import models
from authentication.models import User
import re
from django.db.models.signals import post_save
from django.dispatch import receiver
from api import tasks

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
    
    def __unicode__(self):
        return f'{self.title}'


class Hashtag(models.Model):
    posts = models.ManyToManyField('Post', related_name='hashtags', blank=True)
    name = models.CharField(max_length=100)
    users = models.ManyToManyField(User, related_name='favorites', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('name',)
        # order_by = models.Count(posts)

    def __unicode__(self):
        return f'{self.name}'
    
    def __str__(self):
        return self.name


@receiver(post_save, sender=Post)
def save_hashtag(sender, instance, created, **kwargs):
    regex = r"(?:\s|^)#[A-Za-z\_]+(?:\s|$)"
    hashtags = [i for i in filter(lambda x:re.match(regex,x), instance.body.strip().split())]
    for tag in hashtags:
        hashtag = Hashtag.objects.filter(name=tag)
        if hashtag:
            hashtag = Hashtag.objects.filter(name=tag)[0]
            users = hashtag.users.all()
            if users:
                for usr in users:
                    # Task Send Notification Email
                    tasks.send_a_notification_email(usr.username, usr.email, hashtag.name)
            hashtag.posts.add(instance)
            hashtag.save()
        else:
            newhash = Hashtag.objects.create(name=tag)
            newhash.save()
            newhash.posts.add(instance)
            