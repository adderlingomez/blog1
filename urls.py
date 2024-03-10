from . import views

from django.urls import path

urlpatterns = [
  path("", views.index, name="name"),
  path('storage/<ste:titulo>/<str:cuerpo/', views.storage, name="storage"), 
  path('consultar/<int:id>', views.consultar, name="consultar"),
  path('modificar/<str>:titulo/<int')
]