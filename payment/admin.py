from django.contrib import admin
from .models import *
# Register your models here.
class payment_dataAdmin(admin.ModelAdmin):
    list_display=["refrence_id","flag"]
admin.site.register(payment_data,payment_dataAdmin)
