# Generated by Django 4.2.7 on 2024-03-31 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_alter_order_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='reserved_for',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
