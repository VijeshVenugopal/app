# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 08:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0017_auto_20170103_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetpassword',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 3, 8, 5, 40, 825653)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 3, 8, 5, 40, 823793)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 3, 8, 5, 40, 825076)),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 3, 8, 5, 40, 824534)),
        ),
    ]
