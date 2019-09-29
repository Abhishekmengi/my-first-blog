from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('Two options to be displayed here')


def business(request):
    return HttpResponse('Analysis Tools')


def newsconsumers(request):
    return HttpResponse('Home Page')
