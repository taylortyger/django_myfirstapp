from django.shortcuts import render
from django.http import HttpResponse
from .models import ViewCount
import time
from ipware.ip import get_ip #installed from: sudo pip install django-ipware

def index(request):
    count, countCreated = ViewCount.objects.get_or_create(url_path=request.path)
    count.views += 1
    count.save()
    ip = get_ip(request)
    date = time.strftime("%c")
    html_doc = """
    <!DOCTYPE html>
    <html>
    <head>
    </head>
    <body>
    <h1>Welcome! You are visitor #%s!</h1>
    <p>I can see you... Your current public IP address is: %s</p>
    <p>The current date/time is: %s</p>
    </body>
    </html>
    """ % (count.views, ip, date)
    return HttpResponse(html_doc)