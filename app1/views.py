from django.shortcuts import render
from django.http import *

# Create your views here.



def hello_app(request,name):

    return render(request,"test.html")

