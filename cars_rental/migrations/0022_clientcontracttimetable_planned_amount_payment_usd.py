# Generated by Django 3.0.3 on 2020-04-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0021_clientcontract_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcontracttimetable',
            name='planned_amount_payment_usd',
            field=models.FloatField(null=True, verbose_name='Планова сума платежу, в доларах'),
        ),
    ]
