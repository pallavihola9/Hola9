# Generated by Django 4.0.3 on 2022-12-23 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0002_rename_content_adscomment_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adscomment',
            name='date',
            field=models.CharField(default='2022-12-23', max_length=10),
        ),
    ]
