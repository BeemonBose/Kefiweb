from django.conf.urls import url
from django.contrib import admin
from adminapp import views

urlpatterns = [
    url(r'^$', views.ahome,name='ahome'),
    url(r'^accounts/login/', views.logins,name='logins'),
    url(r'^logout/', views.logouts,name='logouts'),
    url(r'^add_career/', views.add_career,name='add_career'),
    url(r'^edit_career/', views.edit_career,name='edit_career'),
    url(r'^edit_career_detail/(?P<cid>[0-9]+)/$', views.edit_career_detail,name='edit_career_detail'),
    url(r'^delete_career/(?P<cid>[0-9]+)/$', views.delete_career,name='delete_career'),
    url(r'^add_thought/', views.add_thought,name='add_thought'),
    url(r'^edit_thoughts/', views.edit_thoughts,name='edit_thoughts'),
    url(r'^edit_thought_detail/(?P<tid>[0-9]+)/$', views.edit_thought_detail,name='edit_thought_detail'),
    url(r'^add_fav/(?P<tid>[0-9]+)/$', views.add_fav,name='add_fav'),
    url(r'^remove_fav/(?P<tid>[0-9]+)/$', views.remove_fav,name='remove_fav'),
    url(r'^delete_thought/(?P<tid>[0-9]+)/$', views.delete_thought,name='delete_thought'),
    url(r'^add_case_study/', views.add_case_study,name='add_case_study'),
    url(r'^edit_case_study/', views.edit_case_study,name='edit_case_study'),
    url(r'^delete_case/(?P<cid>[0-9]+)/$', views.delete_case,name='delete_case'),
]
