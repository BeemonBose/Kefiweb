# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 11:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0009_auto_20180426_1724'),
    ]

    operations = [
        migrations.RenameField(
            model_name='career',
            old_name='date',
            new_name='uploaded_date',
        ),
        migrations.RenameField(
            model_name='thoughts',
            old_name='date',
            new_name='uploaded_date',
        ),
    ]
