from django.contrib import admin
from .models import *
# Register your models here.
class user_dataAdmin(admin.ModelAdmin):
    list_display=["id","refrence_id"]
admin.site.register(user_data,user_dataAdmin)

class exam_center_dataAdmin(admin.ModelAdmin):
    list_display=["exam_center"]
admin.site.register(exam_center_data,exam_center_dataAdmin)