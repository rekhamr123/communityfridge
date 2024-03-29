# Generated by Django 4.2.6 on 2024-01-04 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridgeapp', '0002_donation'),
    ]

    operations = [
        migrations.CreateModel(
            name='admin_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=50)),
                ('item1', models.CharField(max_length=12)),
                ('item2', models.CharField(max_length=50)),
                ('item3', models.CharField(max_length=100)),
                ('item4', models.CharField(max_length=12)),
                ('item5', models.CharField(max_length=50)),
                ('item6', models.CharField(max_length=100)),
                ('item7', models.CharField(max_length=12)),
                ('item8', models.CharField(max_length=50)),
                ('item9', models.CharField(max_length=100)),
                ('submit_on', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='requesteditems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_name', models.CharField(max_length=30)),
                ('requester_email', models.EmailField(max_length=254)),
                ('requester_phone', models.CharField(max_length=12)),
                ('requester_address', models.CharField(max_length=50)),
                ('request_items', models.CharField(max_length=300)),
                ('request_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
