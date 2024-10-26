# Ex02 Django ORM Web Application
## Date: 26.10.2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![alt text](entity_relationship.png)

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM

```
models.py

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

admin.py

from django.contrib import admin
from .models import bank,bankAdmin
admin.site.register(bank,bankAdmin)
```

## OUTPUT

![alt text](<Screenshot (17).png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
