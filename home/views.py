from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'var': "Test"
    }
    return render(request, 'index.html', context)

def about(request):
    return HttpResponse("This is About Page")

def services(request):
    return HttpResponse("This is Services Page")

def contact(request):
    return HttpResponse("This is Contact Page")