# Generated by Django 4.1.7 on 2023-02-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SupplyManager', '0002_thewall_currentheight_thewall_initialheight_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thewall',
            name='taskID',
            field=models.IntegerField(default=0),
        ),
    ]
