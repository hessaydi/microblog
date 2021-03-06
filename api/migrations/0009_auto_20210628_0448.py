# Generated by Django 3.1.7 on 2021-06-28 04:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180322_1544'),
        ('api', '0008_hashtag_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='users',
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('hashtags', models.ManyToManyField(blank=True, related_name='users', to='api.Hashtag')),
            ],
            options={
                'abstract': False,
            },
            bases=('authentication.user',),
        ),
    ]
