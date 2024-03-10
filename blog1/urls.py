
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', views.index),

    #vista del modulo
    path('post/', 'include'('post.urls'))
 
]

