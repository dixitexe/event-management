# Generated by Django 2.2 on 2020-01-22 03:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpassword',
        ),
    ]
