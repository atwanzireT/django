# Generated by Django 3.2.4 on 2021-06-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_rename_customers_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='logo',
            field=models.ImageField(default='no picture.jpg', upload_to='customers'),
        ),
    ]
