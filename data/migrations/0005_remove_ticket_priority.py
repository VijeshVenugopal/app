# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 06:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20161201_0618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='priority',
        ),
    ]
