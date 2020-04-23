# Generated by Django 3.0.3 on 2020-04-17 10:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0022_clientcontracttimetable_planned_amount_payment_usd'),
    ]

    operations = [
        migrations.AddField(
            model_name='investorcontract',
            name='car',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.Car'),
        ),
        migrations.AddField(
            model_name='investorcontract',
            name='investor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.Investor'),
        ),
        migrations.AddField(
            model_name='investorcontract',
            name='period_1',
            field=models.DateField(null=True, verbose_name='Період 1'),
        ),
        migrations.AddField(
            model_name='investorcontract',
            name='period_2',
            field=models.DateField(null=True, verbose_name='Період 2'),
        ),
        migrations.AddField(
            model_name='investorcontract',
            name='period_3',
            field=models.DateField(null=True, verbose_name='Період 3'),
        ),
        migrations.AddField(
            model_name='investorcontract',
            name='period_4',
            field=models.DateField(null=True, verbose_name='Період 4'),
        ),
        migrations.CreateModel(
            name='InvestorContractTimetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planned_payment_date', models.DateField(null=True, verbose_name='Планова дата платежу')),
                ('planned_amount_payment_usd', models.FloatField(null=True, verbose_name='Планова сума платежу, в доларах')),
                ('real_payment_date', models.DateField(null=True, verbose_name='Дійсна дата платежу')),
                ('amount_paid_usd', models.FloatField(null=True, verbose_name='Оплачена сума, в доларах')),
                ('investor_contract', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.InvestorContract')),
            ],
        ),
    ]
