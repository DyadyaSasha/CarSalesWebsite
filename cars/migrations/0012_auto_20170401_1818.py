# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 15:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0011_auto_20170401_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 1, 15, 18, 19, 864966, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 1, 15, 18, 19, 867689, tzinfo=utc)),
        ),
    ]