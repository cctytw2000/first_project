from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage


# Create your views here.
def index(request):

    return render(request,'home/index.html',locals())


