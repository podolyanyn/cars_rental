# Generated by Django 3.0.3 on 2020-06-24 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0078_auto_20200624_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientcontract',
            name='amount_payment_TO_uah',
            field=models.FloatField(default=0, verbose_name='Сума на ТО, в гривнях'),
        ),
        migrations.AlterField(
            model_name='clientcontract',
            name='balance_TO_uah',
            field=models.FloatField(default=0, verbose_name='Залишок по ТО, в гривнях'),
        ),
        migrations.AlterField(
            model_name='clientcontract',
            name='loan_amount_paid_usd',
            field=models.FloatField(default=0, verbose_name='Виплачена сума кредиту'),
        ),
        migrations.AlterField(
            model_name='clientcontract',
            name='loan_amount_to_be_paid_usd',
            field=models.FloatField(default=0, verbose_name='Cума кредиту до оплати'),
        ),
        migrations.AlterField(
            model_name='clientcontract',
            name='status_body_usd',
            field=models.FloatField(default=0, verbose_name='Стан розрахунку по кредиту. Переплата/прострочка (-)'),
        ),
    ]