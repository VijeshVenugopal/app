# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 04:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20161216_0457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resetpassword',
            name='expiry',
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 59, 29, 771519)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 59, 29, 769830)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 59, 29, 771055)),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 59, 29, 770529)),
        ),
    ]
