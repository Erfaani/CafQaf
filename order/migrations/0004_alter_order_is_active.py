# Generated by Django 4.2.7 on 2023-12-17 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_rename_canceled_order_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
