# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Career,Thoughts,Case_study,News

# Register your models here.
class CareerAdmin(admin.ModelAdmin):
	list_display = ['heading','position']

class ThoughtsAdmin(admin.ModelAdmin):
	list_display = ['heading','favorite','name']

class CasestudyAdmin(admin.ModelAdmin):
	list_display = ['title','category','company']

class NewsstudyAdmin(admin.ModelAdmin):
	list_display = ['title','uploaded_date','news_image']

admin.site.register(Career,CareerAdmin)
admin.site.register(Thoughts,ThoughtsAdmin)
admin.site.register(Case_study,CasestudyAdmin)
admin.site.register(News,NewsstudyAdmin)