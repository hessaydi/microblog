# Generated by Django 3.1.7 on 2021-06-28 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180322_1544'),
        ('api', '0007_hashtag_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='hashtag',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='favorates', to='authentication.User'),
        ),
    ]
