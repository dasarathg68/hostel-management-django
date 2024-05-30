from django import forms  
# Create your models here.

from .models import HostelMember


class HostelForm(forms.ModelForm): # creating a model form class to create Hostel Members object 
	class Meta:
		model=HostelMember
		fields=['Name','Age','Aadhar_No','Residential_Address','Native_Place','Mobile_No'] #attributes of model fields class


class SearchForm(forms.Form): # creating a search form to accept mobile number and search for occupant
	Mobile_No = forms.IntegerField( )# creating an integer field for accepting mobile number as input

