from django.http import HttpResponse
from django.shortcuts import render

def user_home(request):
    return render(request, 'home.html')