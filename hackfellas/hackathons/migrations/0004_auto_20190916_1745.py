# Generated by Django 2.2.4 on 2019-09-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackathons', '0003_auto_20190916_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='hackathon',
            name='price',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='hackathon',
            name='when',
            field=models.CharField(default='', max_length=30),
        ),
    ]
