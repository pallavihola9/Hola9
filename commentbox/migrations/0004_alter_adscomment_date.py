# Generated by Django 4.0.3 on 2022-12-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commentbox', '0003_alter_adscomment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adscomment',
            name='date',
            field=models.CharField(default='2022-12-24', max_length=10),
        ),
    ]