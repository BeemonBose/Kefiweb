# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from djrichtextfield.models import RichTextField
from datetime import datetime
import os
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.
class Career(models.Model):
	uploaded_date = models.CharField(max_length=100)
	position = models.CharField(max_length=250)
	heading = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	experience = models.CharField(max_length=100)
	desc = models.TextField(max_length=500)
	responsibility = models.TextField(max_length=1000)
	requirements = models.TextField(max_length=1000)
	qualification = models.TextField(max_length=1000)

class Thoughts(models.Model):
	uploaded_date = models.CharField(max_length=100,default=datetime.now().strftime("%d %B,%Y"))
	favorite = models.CharField(max_length=50,blank=True)
	heading = models.CharField(max_length=250)
	cover_image=models.ImageField(upload_to='uploads/thought_cover/', help_text="Note: Image resolution should be 1200px x 800px")
	name = models.CharField(max_length=250)
	position = models.CharField(max_length=250)
	linkedin = models.CharField(max_length=100, help_text="For eg: https://www.linkedin.com/in/prasanth-v-092725156/")
	profile_image=models.ImageField(upload_to='uploads/profile_image/', help_text="Note: Image resolution should be 107px x 107px")
	thought = RichTextField(max_length=10000)
	def though(self):
		return self.thought[:100].strip('<p>')

@receiver(pre_delete, sender=Thoughts)
def t_Case_study_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.cover_image.delete(False)
    instance.profile_image.delete(False)

@receiver(models.signals.pre_save, sender=Thoughts)
def t_auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file1 = sender.objects.get(pk=instance.pk).cover_image
        old_file2 = sender.objects.get(pk=instance.pk).profile_image
    except sender.DoesNotExist:
        return False

    new_file1 = instance.cover_image
    if not old_file1 == new_file1:
        if os.path.isfile(old_file1.path):
            os.remove(old_file1.path)

    new_file2 = instance.profile_image
    if not old_file2 == new_file2:
        if os.path.isfile(old_file2.path):
            os.remove(old_file2.path)

CAT_CHOICES = (
    ('Web','Web'),
    ('Mobile', 'Mobile'),
    ('Testing', 'Testing'),
)
class Case_study(models.Model):
	uploaded_date = models.CharField(max_length=100,default=datetime.now().strftime("%d %B,%Y"))
	title = models.CharField(max_length=100)
	company = models.CharField(max_length=250)
	location = models.CharField(max_length=250)
	category=models.CharField(max_length=250, choices=CAT_CHOICES, default='Web')
	challenge = RichTextField(max_length=10000)
	solution = RichTextField(max_length=10000)
	timeline = models.CharField(max_length=200)
	case_image=models.ImageField(upload_to='uploads/case_image/', help_text="Note: Image resolution should be 1200px x 800px")
	screen1=models.ImageField(upload_to='uploads/case_image/screenshots', help_text="Note: Image resolution should be 1200px x 800px",blank=True)
	screen2=models.ImageField(upload_to='uploads/case_image/screenshots', help_text="Note: Image resolution should be 1200px x 800px",blank=True)
	screen3=models.ImageField(upload_to='uploads/case_image/screenshots', help_text="Note: Image resolution should be 1200px x 800px",blank=True)
	screen4=models.ImageField(upload_to='uploads/case_image/screenshots', help_text="Note: Image resolution should be 1200px x 800px",blank=True)
	screen5=models.ImageField(upload_to='uploads/case_image/screenshots', help_text="Note: Image resolution should be 1200px x 800px",blank=True)
	def case_short(self):
		return self.challenge[:400].strip('<p>')

@receiver(pre_delete, sender=Case_study)
def Case_study_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.case_image.delete(False)
    instance.screen1.delete(False)
    instance.screen2.delete(False)
    instance.screen3.delete(False)
    instance.screen4.delete(False)
    instance.screen5.delete(False)

@receiver(models.signals.pre_save, sender=Case_study)
def auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).case_image
        sold_file1 = sender.objects.get(pk=instance.pk).screen1
        old_file2 = sender.objects.get(pk=instance.pk).screen2
        old_file3 = sender.objects.get(pk=instance.pk).screen3
        old_file4 = sender.objects.get(pk=instance.pk).screen4
        old_file5 = sender.objects.get(pk=instance.pk).screen5
    except sender.DoesNotExist:
        return False

    new_file = instance.case_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)

    snew_file1 = instance.screen1
    if not sold_file1 == snew_file1 and not sold_file1 == '':
        if os.path.isfile(sold_file1.path):
            os.remove(sold_file1.path)

    new_file2 = instance.screen2
    if not old_file2 == new_file2 and not old_file2 == '':
        if os.path.isfile(old_file2.path):
            os.remove(old_file2.path)

    new_file3 = instance.screen3
    if not old_file3 == new_file3 and not old_file3 == '':
        if os.path.isfile(old_file3.path):
            os.remove(old_file3.path)

    new_file4 = instance.screen4
    if not old_file4 == new_file4 and not old_file4 == '':
        if os.path.isfile(old_file4.path):
            os.remove(old_file4.path)
            5
    new_file5 = instance.screen5
    if not old_file5 == new_file5 and not old_file5 == '':
        if os.path.isfile(old_file5.path):
            os.remove(old_file5.path)


class News(models.Model):
	uploaded_date = models.CharField(max_length=100,default=datetime.now().strftime("%d %B,%Y"))
	title = models.CharField(max_length=100)
	body = RichTextField(max_length=10000)
	news_image=models.ImageField(upload_to='uploads/news_image/', help_text="Note: Image resolution should be 1200px x 800px")

@receiver(pre_delete, sender=News)
def News_study_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.news_image.delete(False)

@receiver(models.signals.pre_save, sender=News)
def news_auto_delete_file_on_change(sender, instance, **kwargs):
    if not instance.pk:
        return False
    try:
        old_file = sender.objects.get(pk=instance.pk).news_image
    except sender.DoesNotExist:
        return False

    new_file = instance.news_image
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)