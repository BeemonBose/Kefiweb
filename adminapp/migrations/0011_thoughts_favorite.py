# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-27 05:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_auto_20180426_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='thoughts',
            name='favorite',
            field=models.CharField(default='favorite', max_length=50),
            preserve_default=False,
        ),
    ]
