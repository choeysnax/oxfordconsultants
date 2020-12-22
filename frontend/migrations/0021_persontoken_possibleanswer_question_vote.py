# Generated by Django 2.2.10 on 2020-12-22 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0020_person_cv_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=150)),
                ('weight', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PossibleAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordering', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('possible_answers', models.ManyToManyField(to='frontend.PossibleAnswer')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.PossibleAnswer')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.PersonToken')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.Question')),
            ],
        ),
    ]
