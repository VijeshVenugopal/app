# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 06:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0018_auto_20170103_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('chat_id', models.AutoField(primary_key=True, serialize=False)),
                ('chat_from_id', models.IntegerField()),
                ('chat_to_id', models.IntegerField()),
                ('created_date_time', models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 47, 11, 157512))),
                ('deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='resetpassword',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 47, 11, 156995)),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 47, 11, 155272)),
        ),
        migrations.AlterField(
            model_name='ticketattachment',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 47, 11, 156521)),
        ),
        migrations.AlterField(
            model_name='ticketdetail',
            name='created_date_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 11, 47, 11, 155993)),
        ),
    ]
