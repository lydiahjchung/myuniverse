from django.shortcuts import render
from .models import *

# Create your views here.
def main(request):
   return render(request, 'main2.html')

def info(request):
   return render(request, 'info.html')

def concert(request):
   return render(request, 'concert.html')