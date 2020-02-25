# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-25 07:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=250)),
                ('heading', models.CharField(max_length=250)),
                ('location', models.CharField(blank=True, max_length=250)),
                ('experience', models.TextField(max_length=500)),
                ('desc', models.CharField(max_length=250)),
                ('responsibility', models.CharField(max_length=250)),
                ('requirements', models.CharField(max_length=250)),
                ('qualification', models.CharField(max_length=250)),
            ],
        ),
    ]
