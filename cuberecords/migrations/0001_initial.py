# Generated by Django 3.1.5 on 2021-03-26 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spent_time', models.FloatField()),
                ('text', models.TextField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=4096)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation timestamp')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cuberecords.note')),
            ],
        ),
    ]