# Generated by Django 4.0.3 on 2022-12-17 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_telemetrydaa'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=17)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('title', models.CharField(blank=True, max_length=20, null=True)),
                ('Introduction', models.CharField(blank=True, max_length=2000, null=True)),
                ('filename', models.ImageField(blank=True, max_length=232222, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='JobsRequired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.CharField(max_length=200)),
                ('no_of_openings', models.IntegerField(default=None, null=True)),
                ('title', models.CharField(blank=True, max_length=2322, null=True)),
                ('description', models.CharField(max_length=2000, null=True)),
                ('job_responsiblity', models.CharField(max_length=200)),
                ('technical_skills', models.CharField(max_length=200)),
                ('Preferred_qualification', models.CharField(max_length=200, null=True)),
                ('education', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='telemetrydaa',
            name='teleId',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='created_at',
            field=models.CharField(default=datetime.date.today, max_length=150),
        ),
    ]
