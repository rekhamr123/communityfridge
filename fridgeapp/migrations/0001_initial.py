# Generated by Django 4.2.6 on 2023-12-21 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=30)),
                ('memberemail', models.EmailField(max_length=254)),
                ('memberphone', models.CharField(max_length=12)),
                ('memberpassword', models.CharField(max_length=20)),
                ('booked_on', models.DateField(auto_now=True)),
            ],
        ),
    ]
