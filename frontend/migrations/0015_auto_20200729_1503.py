# Generated by Django 2.2.10 on 2020-07-29 15:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('frontend', '0014_upload_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='company_name',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='author',
            field=models.CharField(blank=True, max_length=140),
        ),
    ]
