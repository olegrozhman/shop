# Generated by Django 4.1.4 on 2022-12-17 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_payment_pazorpay_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='pazorpay_order_id',
            new_name='yapay_order_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_id',
            new_name='yapay_payment_id',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_payment_status',
            new_name='yapay_payment_status',
        ),
    ]
