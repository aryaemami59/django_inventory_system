from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World')
    x = 1
    y = 2
    return render(request, 'hello.html', {'name': 'Arya'})


def index(request) -> None:
    return HttpResponse("<h1>Hello index!</h1>")
# render(templates.hello.html)