# Generated by Django 3.2.14 on 2022-07-14 17:25

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_add_cost_and_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
