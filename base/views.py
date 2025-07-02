from django.shortcuts import render


def inicio(request):
    return render(request, 'inicio.html')

def blog(request):
    return render(request, 'blog.html')

def proyectos(request):
    return render(request, 'proyectos.html')

def galeria(request):
    return render(request, 'galeria.html')

def sobre_mi(request):
    return render(request, 'mi.html')
# Create your views here.
