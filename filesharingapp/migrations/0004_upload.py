# Generated by Django 4.0.3 on 2022-04-15 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filesharingapp', '0003_rename_filetype_file_filetypedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('filedata', models.FileField(upload_to='')),
            ],
        ),
    ]
