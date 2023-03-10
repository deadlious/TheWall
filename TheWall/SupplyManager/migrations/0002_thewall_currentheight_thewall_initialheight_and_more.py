# Generated by Django 4.1.7 on 2023-02-24 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyManager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thewall',
            name='currentHeight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thewall',
            name='initialHeight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='thewall',
            name='profile',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='thewall',
            name='section',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AddField(
            model_name='thewall',
            name='taskID',
            field=models.IntegerField(default=None),
        ),
    ]
