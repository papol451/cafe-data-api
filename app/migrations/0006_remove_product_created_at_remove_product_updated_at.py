# Generated by Django 4.2 on 2024-03-24 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='updated_at',
        ),
    ]
