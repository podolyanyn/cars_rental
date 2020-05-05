# Generated by Django 3.0.3 on 2020-05-01 15:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0028_investorcontract_number_periods'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestorContractBodyPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True, verbose_name='Дата платежу')),
                ('sum', models.FloatField(default=0, verbose_name='Сума платежу (погашення тіла боргу)')),
                ('investor_contract', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.InvestorContract')),
            ],
        ),
    ]