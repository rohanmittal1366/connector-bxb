# Generated by Django 3.2.7 on 2021-10-22 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Products'},
        ),
    ]
