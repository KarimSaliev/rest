# Generated by Django 5.0.1 on 2024-02-08 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0005_category_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='icon',
        ),
    ]