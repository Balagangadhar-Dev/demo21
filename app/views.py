from django.shortcuts import render
from .models import cars
# Create your views here.

def index(request):
    cars_details = cars.objects.all()
    return render(request, 'index.html', {'cars_details':cars_details})