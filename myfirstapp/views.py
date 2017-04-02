from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def index(request):
    date = time.strftime("%c")
    return HttpResponse("Right now the date and time is: " + date)