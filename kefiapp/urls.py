from django.conf.urls import url
from django.contrib import admin
from kefiapp import views

urlpatterns = [
    url(r'^$', views.home,name='home'),
    url(r'^about/', views.about,name='about'),
    url(r'^bpo/', views.bpo,name='bpo'),
    url(r'^testing/', views.testing,name='testing'),
    url(r'^why_kefi/', views.why_kefi,name='why_kefi'),
    url(r'^development/', views.development,name='development'),
    url(r'^thoughtroom/', views.thoughtroom,name='thoughtroom'),
    url(r'^thoughts/(?P<tid>[0-9]+)/$', views.thoughts,name='thoughts'),
    url(r'^career/', views.career,name='career'),
    url(r'^careerdetails/(?P<cid>[0-9]+)/$', views.careerdetails,name='careerdetails'),
    url(r'^casestudy/', views.casestudy,name='casestudy'),
    url(r'^cases/(?P<cid>[0-9]+)/$', views.cases,name='cases'),
    url(r'^news/', views.news,name='news'),
]
