# Generated by Django 4.0.3 on 2022-04-08 12:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('filesharingapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='filedata',
        ),
        migrations.AddField(
            model_name='file',
            name='filetype',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='filename',
            field=models.CharField(max_length=20),
        ),
    ]