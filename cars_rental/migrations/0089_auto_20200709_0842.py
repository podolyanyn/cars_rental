# Generated by Django 3.0.3 on 2020-07-09 05:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0088_auto_20200709_0801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontracttimetable',
            name='real_payment_date',
            field=models.DateField(blank=True, default=datetime.date(2020, 7, 9), null=True, verbose_name='Дійсна дата платежу'),
        ),
    ]
