from django.contrib import admin
from.models import photohub

# Register your models here.
@admin.register(photohub)
class photohubAdmin(admin.ModelAdmin):
    list_display=['id','images','date']


