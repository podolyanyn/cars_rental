# Generated by Django 3.0.3 on 2020-05-04 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0030_auto_20200503_0827'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvestorContractTimetable',
            new_name='InvestorContractPercentagePayment',
        ),
    ]