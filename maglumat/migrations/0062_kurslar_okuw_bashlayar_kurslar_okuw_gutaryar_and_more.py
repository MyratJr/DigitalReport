# Generated by Django 4.1.2 on 2023-01-09 06:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0061_alter_ishgarler_is_bashlayar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='kurslar',
            name='okuw_bashlayar',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AddField(
            model_name='kurslar',
            name='okuw_gutaryar',
            field=models.TimeField(default=datetime.time(17, 0)),
        ),
        migrations.AlterField(
            model_name='dinleyjiler',
            name='okuw_bashlayar',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='dinleyjiler',
            name='okuw_gutaryar',
            field=models.TimeField(),
        ),
    ]
