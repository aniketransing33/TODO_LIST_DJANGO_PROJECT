from django.contrib import admin
from app.models import TODO
from .models import *
# Register your models here.
class TODOList(admin.ModelAdmin):
    list_display=['user','title','status','priority']
    list_filter=["user"]
    
admin.site.register(TODO,TODOList)