# Generated by Django 4.1.2 on 2022-10-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0003_rugsatlar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
