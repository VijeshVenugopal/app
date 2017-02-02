# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 06:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0020_auto_20170112_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='chat',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 54, 31, 887829)),
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 54, 31, 887190)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 54, 31, 885530)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 54, 31, 886725)),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 54, 31, 886209)),
        ),
    ]
