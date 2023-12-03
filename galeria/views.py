from django.shortcuts import render

def index(request):
    return render(request, 'galeria/index.html')

def index2(request):
    return render(request, 'galeria/index2.html')

def index3(request):
    return render(request, 'galeria/index3.html')