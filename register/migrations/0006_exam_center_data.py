# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-06 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_user_data_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam_center_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_center', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
