# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-07-01 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20180322_1544'),
        ('api', '0005_auto_20180812_2222'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='upvote',
            unique_together=set([('recipe', 'voted_by')]),
        ),
    ]
