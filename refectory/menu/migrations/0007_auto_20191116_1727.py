# Generated by Django 2.2.7 on 2019-11-16 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0006_auto_20191105_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1', 'Супы'), ('2', 'Гарниры'), ('3', 'Горячие блюда'), ('4', 'Салаты'), ('5', 'Завтраки'), ('6', 'Выпечка'), ('7', 'Дополнительно')], max_length=64),
        ),
    ]
