# Generated by Django 3.0.3 on 2020-06-04 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0067_auto_20200604_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangeratekyiv',
            name='date',
            field=models.DateField(null=True, unique=True, verbose_name='Дата'),
        ),
    ]
