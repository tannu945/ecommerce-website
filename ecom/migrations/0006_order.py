# Generated by Django 3.2.7 on 2021-09-23 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_alter_contact_contact_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('items_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.IntegerField(max_length=10)),
                ('phone_number', models.IntegerField(max_length=10)),
            ],
        ),
    ]
