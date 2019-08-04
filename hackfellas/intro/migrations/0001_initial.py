# Generated by Django 2.2.4 on 2019-08-04 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserRegistrationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_nick_name', models.CharField(max_length=15, unique=True)),
                ('user_email', models.EmailField(max_length=30, unique=True)),
                ('user_age', models.IntegerField(blank=True)),
                ('user_password', models.CharField(max_length=20)),
                ('password_confirm', models.CharField(max_length=20)),
            ],
        ),
    ]
