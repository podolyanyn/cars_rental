# Generated by Django 3.0.3 on 2020-05-30 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0046_auto_20200530_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorcontract',
            name='last_month_percentage',
            field=models.FloatField(null=True, verbose_name='Відсотки за попередній місяць'),
        ),
    ]
