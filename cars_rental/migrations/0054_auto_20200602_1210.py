# Generated by Django 3.0.3 on 2020-06-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0053_auto_20200602_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='passport_data',
            field=models.CharField(max_length=10, null=True, verbose_name='дані  паспорту (серія + номер), чи іншого документу'),
        ),
    ]
