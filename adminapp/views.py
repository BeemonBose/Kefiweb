from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from adminapp.forms import Career_form,Thought_form
from adminapp.models import Career,Thoughts,Case_study
import datetime

# Create your views here.
from django.views.decorators.csrf import csrf_protect

@csrf_protect
def logins(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('ahome')
        else:
            return render(request,'login.html',{'error':'Username and Passwords didn\'t match'})
    else:
        return render(request,'login.html')

def logouts(request):
    logout(request)
    return redirect('ahome')

def ahome(request):
	return render(request, "admin_home.html", {'nbar' : 'home'})
    
def add_thought(request): 
    if request.method == 'POST': 
        log=Thought_form(request.POST, request.FILES)
        if log.is_valid():
            heading=log.cleaned_data['heading']
            cover_image=log.cleaned_data['cover_image']
            name=log.cleaned_data['name']
            position=log.cleaned_data['position']
            linkedin=log.cleaned_data['linkedin']
            profile_image=log.cleaned_data['profile_image']
            thought=log.cleaned_data['thought']
            mydate = datetime.datetime.now()
            th=Thoughts()
            th.uploaded_date=mydate.strftime("%B")+" "+mydate.strftime("%d")+","+mydate.strftime("%Y")
            th.heading=heading
            th.cover_image=cover_image
            th.name=name
            th.position=position
            th.linkedin=linkedin
            th.profile_image=profile_image
            th.thought=thought
            th.save()
            return render(request, "add_thought.html", {'nbar': 'thought'})
    return render(request, "add_thought.html", {'nbar': 'thought'})

def edit_thoughts(request):    
    f_no = Thoughts.objects.filter(favorite="favorite").count()
    thought=Thoughts.objects.filter(favorite="favorite")
    others=Thoughts.objects.exclude(favorite="favorite")
    return render(request, "edit_thoughts.html", {'nbar': 'thought','thoughts':thought,'others':others,'f_no':f_no})

def edit_thought_detail(request,tid):
    th=Thoughts.objects.get(id=tid)
    profile_image=th.profile_image
    cover_image=th.cover_image
    if request.method == 'POST':
        heading=request.POST['heading']
        if request.FILES.get('cover_image'):            
            th.cover_image.delete(save=True)
            cover_image=request.FILES.get('cover_image')
        name=request.POST['name']
        position=request.POST['position']
        linkedin=request.POST['linkedin']
        if request.FILES.get('profile_image'):            
            th.profile_image.delete(save=True)
            profile_image=request.FILES.get('profile_image')
        thought=request.POST['thought']
        th.heading=heading
        th.cover_image=cover_image
        th.name=name
        th.position=position
        th.linkedin=linkedin
        th.profile_image=profile_image
        th.thought=thought
        th.save()
        return redirect('edit_thoughts')
    return render(request, "edit_thought_detail.html", {'nbar': 'thought','thoughts':th})

def add_fav(request,tid):
    f_no = Thoughts.objects.filter(favorite="favorite").count()
    th=Thoughts.objects.get(id=tid)
    th.favorite="favorite"   
    th.save() 
    thought=Thoughts.objects.filter(favorite="favorite")
    others=Thoughts.objects.exclude(favorite="favorite")
    return redirect('edit_thoughts')

def remove_fav(request,tid):
    f_no = Thoughts.objects.filter(favorite="favorite").count()
    th=Thoughts.objects.get(id=tid)
    th.favorite=""   
    th.save() 
    thought=Thoughts.objects.filter(favorite="favorite")
    others=Thoughts.objects.exclude(favorite="favorite")
    return redirect('edit_thoughts')

def delete_thought(request,tid):
    th=Thoughts.objects.get(id=tid)
    th.cover_image.delete(save=True)
    th.profile_image.delete(save=True)
    th.delete()    
    thought=Thoughts.objects.filter(favorite="favorite")
    others=Thoughts.objects.exclude(favorite="favorite")
    return redirect('edit_thoughts')

def add_career(request):
    if request.method == 'POST':
        log=Career_form(request.POST)
        if log.is_valid():
            position=log.cleaned_data['position']
            heading=log.cleaned_data['heading']
            location=log.cleaned_data['location']
            experience=log.cleaned_data['experience']
            desc=log.cleaned_data['desc']
            responsibility=log.cleaned_data['responsibility']
            requirements=log.cleaned_data['requirements']
            qualification=log.cleaned_data['qualification']
            mydate = datetime.datetime.now()
            car=Career()
            car.uploaded_date=mydate.strftime("%B")+" "+mydate.strftime("%d")+","+mydate.strftime("%Y")
            car.position=position
            car.heading=heading
            car.location=location
            car.experience=experience
            car.desc=desc
            car.responsibility=responsibility
            car.requirements=requirements
            car.qualification=qualification
            car.save()
            return render(request, "add_career.html", {'nbar': 'career','success':'success'})
    return render(request, "add_career.html", {'nbar': 'career'})

def edit_career(request):    
    careers = Career.objects.all()
    return render(request, 'edit_career.html',{'nbar': 'career','careers':careers})

def edit_career_detail(request,cid):
    car=Career.objects.get(id=cid)
    if request.method == 'POST':
        log=Career_form(request.POST)
        if log.is_valid():
            position=log.cleaned_data['position']
            heading=log.cleaned_data['heading']
            location=log.cleaned_data['location']
            experience=log.cleaned_data['experience']
            desc=log.cleaned_data['desc']
            responsibility=log.cleaned_data['responsibility']
            requirements=log.cleaned_data['requirements']
            qualification=log.cleaned_data['qualification']
            car.position=position
            car.heading=heading
            car.location=location
            car.experience=experience
            car.desc=desc
            car.responsibility=responsibility
            car.requirements=requirements
            car.qualification=qualification
            car.save()
            return redirect('edit_career')    
    return render(request, 'edit_career_detail.html',{'nbar': 'career','careers':car})

def delete_career(request,cid):
    car=Career.objects.filter(id=cid)
    car.delete()
    careers = Career.objects.all()
    return render(request, 'edit_career.html',{'nbar': 'career','careers':careers})

def add_case_study(request):
    # if request.method == 'POST':
        # log=Career_form(request.POST)
        # if log.is_valid():
            # position=log.cleaned_data['position']
            # heading=log.cleaned_data['heading']
            # location=log.cleaned_data['location']
            # experience=log.cleaned_data['experience']
            # desc=log.cleaned_data['desc']
            # responsibility=log.cleaned_data['responsibility']
            # requirements=log.cleaned_data['requirements']
            # qualification=log.cleaned_data['qualification']
            # mydate = datetime.datetime.now()
            # car=Career()
            # car.uploaded_date=mydate.strftime("%B")+" "+mydate.strftime("%d")+","+mydate.strftime("%Y")
            # car.position=position
            # car.heading=heading
            # car.location=location
            # car.experience=experience
            # car.desc=desc
            # car.responsibility=responsibility
            # car.requirements=requirements
            # car.qualification=qualification
            # car.save()
            # return render(request, "add_career.html", {'nbar': 'case','success':'success'})
    return render(request, "add_case_study.html", {'nbar': 'case'})

def edit_case_study(request):    
    cases = Case_study.objects.all()
    return render(request, 'edit_case_study.html',{'nbar': 'case','cases':cases})

def delete_case(request,cid):
    cas=Case_study.objects.filter(id=cid)
    cas.delete()
    cases = Case_study.objects.all()
    return render(request, 'edit_career.html',{'nbar': 'case','cases':cases})