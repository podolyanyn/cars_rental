# Generated by Django 3.0.3 on 2020-08-04 16:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0107_clientcontractweeklycarreportkyiv'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CarOdesa',
        ),
        migrations.DeleteModel(
            name='ClientContractOdesa',
        ),
        migrations.DeleteModel(
            name='InvestorOdesa',
        ),
        migrations.AlterField(
            model_name='clientcontractkyiv',
            name='car',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.CarKyiv'),
        ),
    ]
