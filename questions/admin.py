from django.contrib import admin
from .models import *
# Register your models here.
class question_dataAdmin(admin.ModelAdmin):
	list_display=["id","question","hint","marks","modified","created"]
admin.site.register(question_data,question_dataAdmin)