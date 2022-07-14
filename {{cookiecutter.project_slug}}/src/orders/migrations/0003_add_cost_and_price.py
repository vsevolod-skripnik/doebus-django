# Generated by Django 3.2.14 on 2022-07-14 16:42

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_item_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='cost',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orderitem',
            name='price',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
