from django.shortcuts import render
from django.http import *

# Create your views here.



def hello_app(request,name):
    data = "Hi {}, Welcome to first view of AWS....".format(name)
    return HttpResponse(data)