# Generated by Django 3.2.7 on 2021-09-23 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order',
            new_name='Orders',
        ),
    ]