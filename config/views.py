from django.shortcuts import render

def maintenance(request):
    return render(request, 'config/maintenance.html')