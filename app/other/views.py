from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(response):
    return HttpResponse('<h2>hello other</h2>')

def intro(response):
    return HttpResponse('<h1>This is the other page!</h1>')