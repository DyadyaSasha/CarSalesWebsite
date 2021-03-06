# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-31 19:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_auto_20170331_1740'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='acount',
            options={'ordering': ['registration_date']},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'ordering': ['price']},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['amount']},
        ),
        migrations.AlterModelOptions(
            name='session',
            options={'ordering': ['user']},
        ),
        migrations.AlterField(
            model_name='acount',
            name='registration_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 31, 19, 22, 0, 927784, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default=datetime.datetime(2017, 3, 31, 19, 22, 0, 930210, tzinfo=utc)),
        ),
        migrations.AlterModelTable(
            name='acount',
            table='acount',
        ),
        migrations.AlterModelTable(
            name='car',
            table='car',
        ),
        migrations.AlterModelTable(
            name='order',
            table='order',
        ),
        migrations.AlterModelTable(
            name='session',
            table='session',
        ),
    ]
