# Generated by Django 4.1.2 on 2022-12-21 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0044_alter_ishgarler_options_alter_ishgarler_is_bashlayar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ishgarler',
            name='each_end',
        ),
        migrations.RemoveField(
            model_name='ishgarler',
            name='each_start',
        ),
    ]
