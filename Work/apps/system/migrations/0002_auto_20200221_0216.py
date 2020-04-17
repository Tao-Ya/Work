# Generated by Django 2.2.6 on 2020-02-21 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentjobs',
            old_name='S_J',
            new_name='S_T',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_U',
            new_name='T_U',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_files',
            new_name='T_files',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_images',
            new_name='T_images',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_text',
            new_name='T_text',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_time',
            new_name='T_time',
        ),
        migrations.RenameField(
            model_name='teacherjobs',
            old_name='J_title',
            new_name='T_title',
        ),
        migrations.RemoveField(
            model_name='teacherjobs',
            name='J_count',
        ),
        migrations.AddField(
            model_name='teacherjobs',
            name='T_count',
            field=models.IntegerField(default=0, verbose_name='完成人数'),
        ),
    ]
