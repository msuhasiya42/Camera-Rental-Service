# Generated by Django 3.1.7 on 2021-04-15 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20210415_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='available',
        ),
    ]