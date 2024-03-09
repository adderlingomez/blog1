
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.site.urls),
    path('post/', views.post, name="index")
 
]
