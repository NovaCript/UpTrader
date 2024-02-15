from django.shortcuts import render
from .models import MenuItem



def index(request):
    return render(request, 'index.html', )