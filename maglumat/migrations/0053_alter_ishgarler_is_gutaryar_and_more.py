# Generated by Django 4.1.2 on 2022-12-27 11:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0052_alter_ishgarler_is_bashlayar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='is_gutaryar',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='obed_bashlayar',
            field=models.TimeField(default=datetime.time(13, 0)),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='obed_gutaryar',
            field=models.TimeField(default=datetime.time(14, 0)),
        ),
    ]
