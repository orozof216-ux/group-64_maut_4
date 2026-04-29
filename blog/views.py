from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def mass(request):
    return HttpResponse('Это мой первый проект на Django')
def emodji(request):
    return HttpResponse('😀😗💀')