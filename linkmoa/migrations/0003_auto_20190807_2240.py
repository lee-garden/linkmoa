# Generated by Django 2.2.4 on 2019-08-07 22:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkmoa', '0002_auto_20190805_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 7, 22, 40, 3, 333084), verbose_name='date_published'),
        ),
    ]
