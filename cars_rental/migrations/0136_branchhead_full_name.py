# Generated by Django 3.0.3 on 2020-11-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0135_auto_20201105_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchhead',
            name='full_name',
            field=models.CharField(max_length=50, null=True, verbose_name='ПІБ'),
        ),
    ]
