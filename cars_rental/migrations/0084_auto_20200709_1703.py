# Generated by Django 3.0.3 on 2020-07-09 14:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0083_auto_20200707_0747'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContractTOToday',
            fields=[
            ],
            options={
                'verbose_name': 'Клієнтський контракт, ТО; введення даних',
                'verbose_name_plural': 'Клієнтський контракт, ТО; введення даних',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cars_rental.clientcontractto',),
        ),
        migrations.AlterField(
            model_name='clientcontractto',
            name='date',
            field=models.DateField(default=datetime.date(2020, 7, 9), null=True, verbose_name='Дата платежу (ТО)'),
        ),
    ]