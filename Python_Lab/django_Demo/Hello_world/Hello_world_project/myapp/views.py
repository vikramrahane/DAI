from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, World")
def my(request):
    return HttpResponse("<h1>Hello,My World</h1>")
def factorial(request):
    return HttpResponse("<h1>Factorial</h1>")