# Generated by Django 2.2.6 on 2019-11-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('1', 'Супы'), ('2', 'Гарниры'), ('2', 'Горячие блюда'), ('3', 'Салаты'), ('4', 'Завтраки'), ('5', 'Выпечка'), ('6', 'Дополнительно')], max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
