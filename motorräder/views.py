from django.shortcuts import render
from django.http import Http404

from .models import Motorräder

def companies(request):
    companies = Motorräder.objects.all()
    return render(request, 'motorräder/motorräder.html', {'motorräder': companies})

def company(request, company):
    try:
        company = Motorräder.objects.get(pk=company)
    except Motorräder.DoesNotExist:
        raise Http404('Company does not exist.')
    return render(request, 'motorräder/motorrad.html', {'motorrad': company})