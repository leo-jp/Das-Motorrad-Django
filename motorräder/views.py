from django.shortcuts import render
from django.http import Http404

from django.views.generic import DetailView, ListView
from .models import Motorräder

class MotorräderView(ListView):
    model = Motorräder
    context_object_name = "motorräder"
    template_name = "motorräder/motorräder.html"
    
class MotorradView(DetailView):
    model = Motorräder
    context_object_name = "motorrad"
    template_name = "motorräder/motorrad.html"