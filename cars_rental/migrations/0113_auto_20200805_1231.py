# Generated by Django 3.0.3 on 2020-08-05 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0112_auto_20200805_1116'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvestorContract',
            new_name='InvestorContractKyiv',
        ),
        migrations.AlterModelOptions(
            name='investorcontractkyiv',
            options={'verbose_name': 'Інвесторський контракт (Київ)', 'verbose_name_plural': 'Інвесторські контракти (Київ)'},
        ),
    ]
