from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('Index page')


def maintenance(request):
    return render(request, 'config/maintenance.html')