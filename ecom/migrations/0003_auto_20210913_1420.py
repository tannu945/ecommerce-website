# Generated by Django 3.2.7 on 2021-09-13 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0002_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='id',
        ),
        migrations.AddField(
            model_name='contact',
            name='contact_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
