# Generated by Django 4.2.7 on 2024-04-01 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_order_reserved_for'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='reserved_for',
        ),
    ]
