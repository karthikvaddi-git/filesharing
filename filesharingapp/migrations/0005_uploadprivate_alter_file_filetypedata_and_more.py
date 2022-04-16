# Generated by Django 4.0.3 on 2022-04-15 18:18

from django.db import migrations, models
import filesharingapp.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('filesharingapp', '0004_upload'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadPrivate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('filedata', models.FileField(storage=filesharingapp.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='file',
            name='filetypedata',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='upload',
            name='filedata',
            field=models.FileField(storage=filesharingapp.storage_backends.PublicMediaStorage(), upload_to=''),
        ),
    ]