from django.shortcuts import path
from . import views

# Create your views here.

urlpatterns = [
  post("", views.index, name="post" )
]