# Generated by Django 3.0.3 on 2020-06-24 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0074_auto_20200624_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontract',
            name='amount_payment_uah',
            field=models.FloatField(default=0, verbose_name='Сума платежу в гривнях'),
        ),
    ]
