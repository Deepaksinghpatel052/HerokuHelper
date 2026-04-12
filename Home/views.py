from django.shortcuts import render
from django.conf import settings

def home(request):
    return render(request, 'home.html',{"BASE_URL":settings.BASE_URL})