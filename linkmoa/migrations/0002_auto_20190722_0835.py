# Generated by Django 2.2.3 on 2019-07-22 08:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linkmoa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 22, 8, 35, 20, 227114), verbose_name='date_published'),
        ),
    ]