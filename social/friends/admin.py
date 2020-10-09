from django.contrib import admin
from .models import Friend
# Register your models here.
class FriendAdmin(admin.ModelAdmin):
    list_display = ['user','friend']
admin.site.register(Friend, FriendAdmin)