from django.contrib import admin
from .models import *

# Register your models here.
class quiz_dataAdmin(admin.ModelAdmin):
	list_display=["id","quiz_name","quiz_description","quiz_image","quiz_type","modified","created"]
admin.site.register(quiz_data,quiz_dataAdmin)