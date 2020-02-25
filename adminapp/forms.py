from django import forms

class Career_form(forms.Form):
	position = forms.CharField(max_length=250)
	heading = forms.CharField(max_length=250)
	location = forms.CharField(max_length=250)
	experience = forms.CharField(max_length=100)
	desc = forms.CharField(max_length=500)
	responsibility = forms.CharField(max_length=1000)
	requirements = forms.CharField(max_length=1000)
	qualification = forms.CharField(max_length=1000)

class Thought_form(forms.Form):
	heading = forms.CharField(max_length=250)
	cover_image=forms.ImageField()
	name = forms.CharField(max_length=250)
	position = forms.CharField(max_length=250)
	linkedin = forms.CharField(max_length=100)
	profile_image=forms.ImageField()
	thought = forms.CharField(max_length=10000)