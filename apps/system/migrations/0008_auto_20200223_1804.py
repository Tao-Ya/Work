# Generated by Django 2.2.6 on 2020-02-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0007_auto_20200223_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentjobs',
            name='S_is',
            field=models.IntegerField(default=0, verbose_name='是否通过'),
        ),
    ]
