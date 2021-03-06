# Generated by Django 3.1.7 on 2021-03-20 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20210320_1120'),
    ]

    operations = [
        migrations.CreateModel(
            name='userCustomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=20)),
                ('mobile_no', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=50)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameModel(
            old_name='RegCustomer',
            new_name='vendorCustomer',
        ),
    ]
