# Generated by Django 3.0.3 on 2020-08-05 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0119_investorlviv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorcontractkyiv',
            name='car',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='cars_rental.CarKyiv'),
        ),
    ]
