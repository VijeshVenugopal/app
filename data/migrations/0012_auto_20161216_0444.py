# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 04:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_auto_20161206_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 44, 12, 569852)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 44, 12, 571068)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='file_name',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 44, 12, 570553)),
        ),
    ]
