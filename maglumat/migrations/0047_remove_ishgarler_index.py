# Generated by Django 4.1.2 on 2022-12-26 11:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0046_ishgarler_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ishgarler',
            name='index',
        ),
    ]
