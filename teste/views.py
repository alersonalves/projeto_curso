from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Olá, Mundo! Agora é na Web.")

def novo(request):
    return HttpResponse("Esta é uma página de teste")