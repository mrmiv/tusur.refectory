# Generated by Django 2.2.7 on 2019-11-17 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20191117_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='basket',
            options={'verbose_name': 'Продукт заказа', 'verbose_name_plural': 'Продукты заказа'},
        ),
        migrations.AlterModelTable(
            name='basket',
            table='orders_order_products',
        ),
    ]
