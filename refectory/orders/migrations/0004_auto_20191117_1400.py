# Generated by Django 2.2.7 on 2019-11-17 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20191117_1317'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='user',
        ),
    ]
