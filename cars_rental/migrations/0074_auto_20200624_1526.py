# Generated by Django 3.0.3 on 2020-06-24 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars_rental', '0073_auto_20200624_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientcontract',
            old_name='loan_amount_paid',
            new_name='loan_amount_paid_usd',
        ),
        migrations.RenameField(
            model_name='clientcontract',
            old_name='loan_amount_to_be_paid',
            new_name='loan_amount_to_be_paid_usd',
        ),
        migrations.RenameField(
            model_name='clientcontract',
            old_name='status_body',
            new_name='status_body_usd',
        ),
    ]