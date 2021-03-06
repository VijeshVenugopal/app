# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 04:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20161216_0444'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetPassword',
            fields=[
                ('reset_password_id', models.AutoField(primary_key=True, serialize=False)),
                ('reset_code', models.CharField(max_length=100)),
                ('created_user_id', models.IntegerField()),
                ('created_date_time', models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 57, 24, 303580))),
                ('deleted', models.BooleanField(default=False)),
                ('expiry', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 57, 24, 301893)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 57, 24, 303130)),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 12, 16, 4, 57, 24, 302617)),
        ),
    ]
