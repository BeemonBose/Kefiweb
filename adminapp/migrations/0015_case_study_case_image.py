# Generated by Django 2.2 on 2019-06-20 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0014_auto_20190619_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='case_study',
            name='case_image',
            field=models.ImageField(default=1, upload_to='uploads/case_image/'),
            preserve_default=False,
        ),
    ]