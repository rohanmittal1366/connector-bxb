# Generated by Django 3.2.7 on 2021-10-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_merge_0003_auto_20211022_2257_0003_auto_20211023_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Food', 'Food'), ('Clothes', 'Clothes'), ('Medicine', 'Medicine')], max_length=20, null=True),
        ),
    ]
