# Generated by Django 4.1.2 on 2022-12-27 11:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0050_alter_ishgarler_each_end_alter_ishgarler_each_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='each_end',
            field=models.DateField(default=datetime.date(2022, 12, 27)),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='each_start',
            field=models.DateField(default=datetime.date(2022, 12, 27)),
        ),
    ]
