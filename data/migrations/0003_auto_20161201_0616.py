# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20161128_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketstatus',
            name='status_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
