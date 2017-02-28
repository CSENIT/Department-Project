from __future__ import unicode_literals
from django.db import models
# Create your models here.
class subject(models.Model):
    	subject_name = models.CharField(max_length=50)
class question_data(models.Model):
	question=models.CharField(max_length=512,null=False,blank=True)
	hint=models.CharField(max_length=255,null=False,blank=True)
	marks=models.IntegerField(default=0)
	subjects=models.ManyToManyField(subject,null=True,blank=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	option1= models.CharField(max_length=512,null=False,blank=True)
	option2= models.CharField(max_length=512,null=False,blank=True)
	option3= models.CharField(max_length=512,null=False,blank=True)
	option4= models.CharField(max_length=512,null=False,blank=True)

