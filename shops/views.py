from django.http import HttpResponse

def index(request):
    return HttpResponse("You are at the shop home page")

def products(request):
    return HttpResponse('You are at the products list page')

