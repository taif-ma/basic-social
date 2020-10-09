from django.urls import path, include
#from userprofile.urls import 
from .views import *

app_name = "core"

urlpatterns = [
    path('', home, name="home"),
    path('profile/', include('userprofile.urls'), name="userprofile")
]
