# Generated by Django 2.2.2 on 2019-07-19 06:16

import datetime
from django.db import migrations, models
import tagging.fields


class Migration(migrations.Migration):

    dependencies = [
        ('linkmoa', '0012_auto_20190718_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='memo',
            name='tag',
            field=tagging.fields.TagField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='memo',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 19, 15, 16, 16, 95190), verbose_name='date_published'),
        ),
    ]