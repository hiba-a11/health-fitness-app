# tracker/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'tracker/home.html')

def calculators(request):
    return render(request, 'tracker/calc.html')