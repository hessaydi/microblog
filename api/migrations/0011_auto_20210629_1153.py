# Generated by Django 3.1.7 on 2021-06-29 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20210628_1138'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='category',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='review',
            name='recipe',
        ),
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='recipe',
        ),
        migrations.RemoveField(
            model_name='upvote',
            name='voted_by',
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Upvote',
        ),
    ]
