# Generated by Django 3.2.4 on 2021-06-22 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customers',
            new_name='Customer',
        ),
    ]
