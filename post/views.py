from django.shortcuts import render
from  django.http import HttpResponse
from .models import post


def index(request):
  posts = post()

  return HttpResponse('lista de post')

def storange(request, titulo, cuerpo):
  

  post = post(titulo=titulo, cuarpo=cuerpo)
  post.save()

  #trabajar con el modelo

  return HttpResponse('guardamos el modelo y no mostramos la vista')

def consultar(request,id):
  post = post.objects.get(id = id)
  print f"\ntitulo:(post.titulo)\ncuerpo:(post.cuerpo)\nfecha:(post.fecha)"
  return HttpResponse("titulo: (post.titulo), cuerpo: (post.cuerpo), fecha: (post.fecha)")



def actualizar(request, consulta_id)
post = post.objects.get(id=consulta_id)
if campo =="titulo":
  post.titulo = valor
elif campo == "cuerpo":
  post.cuerpo = valor
  post.save()
  return HttpResponse(f"guardamos los titulos: (post.titulo)... cuerpo(post.cuerpo)") 

def eliminar(request, consulta_id):
  post = post.objects.get(id=consulta_id)
  post.delete()
  return HttpResponse("post eliminado")
