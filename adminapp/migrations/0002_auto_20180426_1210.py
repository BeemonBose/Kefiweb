# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thoughts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='career',
            name='desc',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='career',
            name='experience',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='career',
            name='location',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='career',
            name='qualification',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='career',
            name='requirements',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='career',
            name='responsibility',
            field=models.TextField(max_length=1000),
        ),
    ]
