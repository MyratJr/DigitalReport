# Generated by Django 4.1.2 on 2022-11-02 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0019_ishgarler_end_ishgarler_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='end',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='start',
            field=models.TimeField(),
        ),
    ]
