from django.contrib import admin
from .models import *

# Register your models here.
class quiz_dataAdmin(admin.ModelAdmin):
	list_display=["id","name","description","image","quiz_type","marks","modified","created"]
admin.site.register(quiz_data,quiz_dataAdmin)