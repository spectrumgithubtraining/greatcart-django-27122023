# Generated by Django 4.1.2 on 2023-12-27 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_rename_payment_id_order_payment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
    ]
