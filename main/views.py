from django.shortcuts import render
from django.http import HttpResponse
from .json_parser import data
# what is the difference between .json import data and . import json??


def basic(request):
    return render(request, 'main/index.html', {'data': data})

def first(request):
    return render(request, 'main/first.html', {'data': data})

def second(request):
    return render(request, 'main/second.html', {'data': data})

def third(request):
    return render(request, 'main/third.html', {'data': data})

def fourth(request):
    return render(request, 'main/fourth.html', {'data': data})

def fifth(request):
    return render(request, 'main/fifth.html', {'data': data})

def sixth(request):
    return render(request, 'main/sixth.html', {'data': data})


def seventh(request):
    return render(request, 'main/seventh.html', {'data': data})


def eighth(request):
    return render(request, 'main/eighth.html', {'data': data})

def ninth(request):
    return render(request, 'main/ninth.html', {'data': data})


def tenth(request):
    return render(request, 'main/tenth.html', {'data': data})

def eleventh(request):
    return render(request, 'main/eleventh.html', {'data': data})

def twelfth(request):
    return render(request, 'main/twelfth.html', {'data': data})

def thirtieth(request):
    return render(request, 'main/thirtieth.html', {'data': data})







