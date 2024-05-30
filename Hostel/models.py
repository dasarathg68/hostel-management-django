from django.db import models

# Create your models here.
class HostelMember(models.Model):
	Aadhar_No=models.IntegerField()#field for accepting aadhar number
	Name=models.CharField(max_length=100)#field for accepting occupant name
	Age=models.IntegerField()#field for accepting age
	Residential_Address=models.CharField(max_length=100)#field for accepting address
	Native_Place=models.CharField(max_length=100)#field for acceping native place
	Mobile_No=models.IntegerField()#field for accepting mobile number

	def __str__(self): #returns the foreign key of the model class
		return self.Name