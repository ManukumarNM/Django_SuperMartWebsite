# Generated by Django 3.2.10 on 2021-12-21 07:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_variation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variation',
            old_name='product',
            new_name='product_name',
        ),
    ]
