# Generated by Django 2.2.6 on 2019-11-05 04:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_auto_20191104_2012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='additionally',
        ),
        migrations.AddField(
            model_name='product',
            name='additional',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='full_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]