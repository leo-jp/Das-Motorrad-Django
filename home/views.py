from django.shortcuts import render
from django.http import HttpResponse
from datetime import date, datetime

def home(request):
    return render(request, 'home/index.html', {'today': datetime.today()})