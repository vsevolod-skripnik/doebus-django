# Generated by Django 3.2.14 on 2022-07-14 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='data',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]
