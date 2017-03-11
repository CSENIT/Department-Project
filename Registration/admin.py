from django.contrib import admin
from .models import *
# Register your models here.
class student_dataAdmin(admin.ModelAdmin):
	list_display=["fname","lname","rollNumber","email","mobile"]

admin.site.register(student_data,student_dataAdmin)

class BranchAdmin(admin.ModelAdmin):
	list_display=["branchName"]

admin.site.register(Branch,BranchAdmin)

class SemesterAdmin(admin.ModelAdmin):
	list_display=["semesterName"]

admin.site.register(Semester,SemesterAdmin)

