# Generated by Django 3.2.14 on 2022-07-14 18:44

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_drop_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='status',
            field=models.CharField(default='CREATED', max_length=255),
        ),
    ]
