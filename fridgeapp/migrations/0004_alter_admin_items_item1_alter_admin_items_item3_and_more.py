# Generated by Django 4.2.6 on 2024-01-04 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fridgeapp', '0003_admin_items_requesteditems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin_items',
            name='item1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_items',
            name='item3',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_items',
            name='item4',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_items',
            name='item6',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_items',
            name='item7',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='admin_items',
            name='item9',
            field=models.CharField(max_length=50),
        ),
    ]
