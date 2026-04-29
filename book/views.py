from django.shortcuts import render
from django.http import HttpResponse

def quote1(request):
    return HttpResponse("Не ошибается только тот, кто ничего не делает.")

def quote2(request):
    return HttpResponse("Знание — сила.")

def quote3(request):
    return HttpResponse("Всегда стремись к большему.")
# Create your views here.
