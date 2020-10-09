from django.contrib import admin
from .models import *
# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ['id']
admin.site.register(Room, RoomAdmin)