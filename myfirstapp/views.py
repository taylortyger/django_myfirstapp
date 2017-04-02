from django.shortcuts import render
from django.http import HttpResponse
from .models import ViewCount

import time
from ipware.ip import get_ip

def index(request):
    count, countCreated = ViewCount.objects.get_or_create(url_path=request.path)
    count.views += 1
    count.save()
    ip = get_ip(request)
    date = time.strftime("%c")
    return HttpResponse("Right now the date and time is: " + date + "<br />Your IP address is: " + ip + "<br />Visting path: " + str(request.path) + "<br />Page Views: " + str(count.views))