# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-03 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_auto_20160903_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment_data',
            name='last_transaction',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
