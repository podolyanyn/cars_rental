# Generated by Django 3.0.3 on 2020-11-05 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0140_test'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='test_field',
            field=models.CharField(default='Шевченко Юрій', max_length=25, verbose_name='тест'),
        ),
    ]