# Generated by Django 4.1.2 on 2022-11-21 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maglumat', '0041_alter_ishgarler_balnoy_gornush_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ishgarler',
            name='balnoy_gornush',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='maglumat.rugsatlar'),
        ),
        migrations.AlterField(
            model_name='ishgarler',
            name='wezipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maglumat.wezipeler'),
        ),
    ]
