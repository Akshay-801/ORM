from django.db import models
from django.contrib import admin

class bank(models.Model):
	name=models.CharField(max_length=20)
	email=models.EmailField()
	phno =models.IntegerField()
	aadhar=models.IntegerField(primary_key='aadhar')
	dob=models.DateField()
	passno=models.IntegerField()

class bankAdmin(admin.ModelAdmin):
	list_display=('name','email','phno','aadhar','dob','passno')
