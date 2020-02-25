	# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from adminapp.models import Career,Thoughts,Case_study,News
from django.core.paginator import Paginator

# Create your views here.

def home(request):
	thought=Thoughts.objects.order_by('-id')[:3]
	case_study=Case_study.objects.order_by('-id')[:3]
	return render(request, "index.html",{'thoughts':thought,'case_study':case_study})

def about(request):
    return render(request, "about.html")

def bpo(request):
	return render(request, "bpo.html")

def testing(request):
	return render(request, "testing.html")

def why_kefi(request):
	return render(request, "why_kefi.html")

def development(request):
	return render(request, "development.html")

def thoughtroom(request):
	posts_list = Thoughts.objects.all()
	paginator = Paginator(posts_list, 6)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	return render(request, 'thoughtroom.html',{ 'posts' : posts })
	
def thoughts(request,tid):	
	thought=Thoughts.objects.get(id=tid)
	return render(request, "thoughts.html",{'thoughts':thought})

# def career(request):
#     c_no = Career.objects.all().count()
#     p = c_no/9
#     pno = int(request.GET.get('page', 1))  # Set 'name' as a default value
#     cid = pno - 1
#     careers = Career.objects.all()[cid*9:cid*9+9]
#     return render(request, "career.html",{'careers':careers,'tot_p':p,'page_no':pno})

def career(request):
	posts_list = Career.objects.all()
	paginator = Paginator(posts_list, 12)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	return render(request, 'career.html',{ 'posts' : posts })

def careerdetails(request,cid):
	car=Career.objects.get(id=cid)
	resp= car.responsibility.strip(".").split(".")
	req= car.requirements.strip(".").split(".")
	qual= car.qualification.strip(".").split(".")
	return render(request, "careerdetails.html",{'careers':car,'resp':resp,'req':req,'qual':qual})


def casestudy(request):
	posts_list = Case_study.objects.all()
	paginator = Paginator(posts_list, 6)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	return render(request, 'casestudy.html',{ 'posts' : posts })

def cases(request,cid):	
	case_study=Case_study.objects.get(id=cid)
	return render(request, "case.html",{'case_study':case_study})

def news(request):
	posts_list = News.objects.all()
	print(posts_list)
	paginator = Paginator(posts_list, 12)
	try:
		page = int(request.GET.get('page', '1'))
	except:
		page = 1
	try:
		posts = paginator.page(page)
	except(EmptyPage, InvalidPage):
		posts = paginator.page(paginator.num_pages)
	return render(request, 'news.html',{ 'posts' : posts })