# Generated by Django 3.1.7 on 2021-04-10 03:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='status',
            new_name='order_status',
        ),
    ]