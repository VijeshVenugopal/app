# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 06:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20161201_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('ticket_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('assigned_user_id', models.IntegerField()),
                ('created_user_id', models.IntegerField()),
                ('created_date_time', models.DateTimeField()),
                ('deleted', models.BooleanField()),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TicketPriority')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TicketStatus')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TicketType')),
            ],
        ),
        migrations.CreateModel(
            name='TicketAttachment',
            fields=[
                ('ticket_attachment_id', models.AutoField(primary_key=True, serialize=False)),
                ('original_file_name', models.CharField(max_length=200)),
                ('file_name', models.CharField(max_length=50)),
                ('created_user_id', models.IntegerField()),
                ('created_date_time', models.DateTimeField()),
                ('deleted', models.BooleanField()),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Ticket')),
            ],
        ),
        migrations.CreateModel(
            name='TicketDetail',
            fields=[
                ('ticket_detail_id', models.AutoField(primary_key=True, serialize=False)),
                ('ticket_text', models.TextField()),
                ('created_user_id', models.IntegerField()),
                ('created_date_time', models.DateTimeField()),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TicketStatus')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Ticket')),
            ],
        ),
        migrations.AddField(
            model_name='ticketattachment',
            name='ticket_detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.TicketDetail'),
        ),
    ]