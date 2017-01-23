from __future__ import unicode_literals

from django.db import models

# Create your models here.
class quiz_data(models.Model):
	name=models.CharField(max_length=24,null=False,blank=False)
	description=models.CharField(max_length=512,null=False,blank=True)
	image=models.ImageField(upload_to="quiz_image/",max_length=512,null=False,blank=True)
	quiz_type=models.IntegerField(default=0)
	marks=models.IntegerField(default=100)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)