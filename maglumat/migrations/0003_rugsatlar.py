# Generated by Django 4.1.2 on 2022-10-24 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0002_ishgarler'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rugsatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rugsat_at', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['Rugsat_at'],
            },
        ),
    ]
