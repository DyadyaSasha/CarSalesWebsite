# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 16:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0017_auto_20170401_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 1, 16, 39, 49, 725949, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2017, 4, 1, 16, 39, 49, 728629, tzinfo=utc)),
        ),
    ]