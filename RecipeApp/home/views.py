from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    context={"page":"Home"}
    return render(request, 'home/index.html',context)

def success_page(request):
    context={'page':'Success'}
    return render(request, 'home/success.html',context)

def about(request):
    context={"page":"About"}
    return render(request, 'home/about.html',context)