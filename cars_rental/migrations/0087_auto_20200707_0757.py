# Generated by Django 3.0.3 on 2020-07-07 04:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0086_auto_20200708_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontracttimetable',
            name='real_payment_date',
            field=models.DateField(blank=True, null=True, verbose_name='Дійсна дата платежу'),
        ),
        migrations.AlterField(
            model_name='clientcontractto',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 7), null=True, verbose_name='Дата платежу (ТО)'),
        ),
    ]
