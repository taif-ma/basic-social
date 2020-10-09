from django.urls import path
from .views import *

app_name = "profile"

urlpatterns = [
    path('edit-profile', ProfileEditView.as_view(), name="edit-profile"),
    path('<slug:username>', TimelineView.as_view(), name="user-timeline"),
    #path('search', ProfileList.as_view(), name="profiles"),
    path('search', SearchProfile, name="profiles"),
]
