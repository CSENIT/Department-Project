from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student_data(models.Model):
	password=models.CharField(max_length=512,null=False,blank=False)
	enrollmentNumber=models.PositiveSmallIntegerField(null=False,blank=False)
	rollNumber=models.PositiveSmallIntegerField(null=False,blank=False)
	fname= models.CharField(max_length=120,null=False,blank=False)
	lname= models.CharField(max_length=120,null=False,blank=False)
	mobile=models.PositiveSmallIntegerField(null=False,blank=False)
	email=models.CharField(max_length=120,null=False,blank=False)
	Branch = models.ForeignKey('Branch')
	smester = models.ForeignKey('Semester')
	mobileVerified= models.BooleanField(default=False)
	emailVerified= models.BooleanField(default=False)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)

class Branch(models.Model):	
	branchId=models.IntegerField(primary_key=True)
	branchName=models.CharField(max_length=120,null=False,blank=False)

class Semester(models.Model):
	semesterId=models.IntegerField(primary_key=True)
	semesterName=models.CharField(max_length=120,null=False,blank=False)


