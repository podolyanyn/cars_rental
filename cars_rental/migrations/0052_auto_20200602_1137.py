# Generated by Django 3.0.3 on 2020-06-02 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0051_auto_20200602_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontractto',
            name='note',
            field=models.CharField(max_length=100, null=True, verbose_name='Примітки'),
        ),
    ]