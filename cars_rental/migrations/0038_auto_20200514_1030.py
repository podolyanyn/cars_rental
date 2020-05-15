# Generated by Django 3.0.3 on 2020-05-14 07:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0037_auto_20200513_1826'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientcontract',
            name='amount_payment_TO_uah',
            field=models.FloatField(null=True, verbose_name='Сума на ТО, в гривнях'),
        ),
        migrations.AddField(
            model_name='clientcontract',
            name='balance_TO_uah',
            field=models.FloatField(null=True, verbose_name='Залишок по ТО, в гривнях'),
        ),
        migrations.CreateModel(
            name='ClientContractTO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата платежу (ТО)')),
                ('sum', models.FloatField(null=True, verbose_name='Сума платежу (ТО)')),
                ('client_contract', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.ClientContract')),
            ],
        ),
    ]
