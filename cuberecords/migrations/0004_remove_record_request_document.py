# Generated by Django 3.1.5 on 2021-03-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cuberecords', '0003_record_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record_request',
            name='document',
        ),
    ]
