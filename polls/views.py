from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

def index(request):
    return HttpResponse("Hello world, a75c57ea you're at the polls index .")
