from django.shortcuts import render
from django.http import HttpResponse
from .models import Image, Category, Company

def index(request):
    return HttpResponse("<h1>Firma Ana Sayfa</h1>")

def detail(request, company_id):
    image = Image.objects.filter(id = company_id)
    return HttpResponse('<img src="' + image[0].path + '" />')