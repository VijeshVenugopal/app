# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-02 12:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20161201_0652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]