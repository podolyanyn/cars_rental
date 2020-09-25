# Generated by Django 3.0.3 on 2020-09-25 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0126_clientcontractweeklycartoreportkyiv'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientContractFullCarReportKyiv',
            fields=[
            ],
            options={
                'verbose_name': 'Клієнтський контракт (Київ), звіт по авто, повний',
                'verbose_name_plural': 'Клієнтські контракти (Київ), звіт по авто, повний',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('cars_rental.clientcontractkyiv',),
        ),
    ]
