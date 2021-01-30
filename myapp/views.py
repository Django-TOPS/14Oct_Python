from django.shortcuts import render, Http404, HttpResponse

# Create your views here.

def index(request):
    return render(request,'index.html')

def notfound(request):
    return render(request,'404.html')