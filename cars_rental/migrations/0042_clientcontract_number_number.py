# Generated by Django 3.0.3 on 2020-05-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0041_exchangeratelviv_exchangerateodesa'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcontract',
            name='number_number',
            field=models.IntegerField(null=True, verbose_name='Номер номеру контракту'),
        ),
    ]