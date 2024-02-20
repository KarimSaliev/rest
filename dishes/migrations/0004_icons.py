# Generated by Django 5.0.1 on 2024-02-08 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dishes', '0003_category_dish_description_dish_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref', models.CharField(max_length=128, unique=True)),
            ],
            options={
                'verbose_name': 'icon',
                'verbose_name_plural': 'icons',
            },
        ),
    ]