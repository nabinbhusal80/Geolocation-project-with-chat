# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-03 15:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_auto_20170602_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='messageclass',
            name='seen_case',
            field=models.BooleanField(default=False),
        ),
    ]