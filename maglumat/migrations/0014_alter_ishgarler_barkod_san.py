# Generated by Django 4.1.2 on 2022-10-31 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0013_wezipeler_is_gutar_wezipeler_obed_basla_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='barkod_san',
            field=models.DecimalField(decimal_places=0, max_digits=13),
        ),
    ]
