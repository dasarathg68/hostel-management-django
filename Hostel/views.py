from django.shortcuts import render
from .models import HostelMember
from .forms import HostelForm,SearchForm	
# Create your views here.
def create_form_view(request): #creating an object for the Hostel members class

	form=HostelForm(request.POST or None)

	if form.is_valid():#checking if the form is valid
		form.save()# saving the form
		form=HostelForm()
	context={'form':form} #context for the html file
	return render(request,'createnew.html',context) #rendering the html file

def home_view(request): 
	return render(request,"home.html")#rendering the home page of the application

def search_view(request):
	if request.method=='POST': #checking if the method is post
		form=SearchForm(request.POST)
		
		if form.is_valid():#checking if the form is valid
			mobno=form.cleaned_data['Mobile_No'] #obtaining the mobile number for the given data

			#checks if the data already exists in the database
			members=HostelMember.objects.filter(Mobile_No=mobno)
			#return render(request,'userdata.html',{'member':member})
			#hostel=HostelMember.objects.all()
			return render(request,'userdata.html',{'members':members	})

				 	  
	else:
		form=SearchForm()
	return render(request,'search.html',{'form':form})#rendering the search view

def index(request):
	hostel=HostelMember.objects.all()
	return render(request,'index.html',{'hostel':hostel	})#rendering the database index view