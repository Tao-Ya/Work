# Generated by Django 2.2.6 on 2020-02-04 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_is_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_rank',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
