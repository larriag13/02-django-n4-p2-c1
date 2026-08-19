from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def vista1(request):
    return HttpResponse("<h1>Vista 1 App1</h1>"
    "<p style='color:blue'>Todo lo que necesitas</p>")