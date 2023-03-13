from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def first_app1(request):
    return HttpResponse('<h1>This is first function in app1</h1>')



def first_app2(request):
    return HttpResponse('<h2>This is first function in app2</h2>')


def second_app1(request):
    return HttpResponse('<h1><marquee>This is my second function in app1</marquee></h1>')