# Generated by Django 5.1 on 2024-09-07 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0002_alter_employee_address_alter_employee_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='contact',
            field=models.CharField(max_length=50),
        ),
    ]
