# Generated by Django 2.2.10 on 2020-07-08 17:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('frontend', '0010_auto_20200708_1225'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
