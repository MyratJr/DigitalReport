# Generated by Django 4.1.2 on 2022-11-04 11:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0023_days'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='days',
            options={'ordering': ['day']},
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='end',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='start',
            field=models.TimeField(default=datetime.time(9, 0)),
        ),
    ]
