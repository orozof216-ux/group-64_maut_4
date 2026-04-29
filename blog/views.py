from django.http import HttpResponse

def message(request):
    return HttpResponse('Это мой первый проект на Django')

def emoji(request):
    return HttpResponse('😀😗💀')