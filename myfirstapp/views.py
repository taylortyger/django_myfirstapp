from django.shortcuts import render
from django.http import HttpResponse
from .models import ViewCount
from .models import Joke
from random import randint
import time
from ipware.ip import get_ip #installed from: sudo pip install django-ipware


def getRandomJoke():
    jokes = Joke.objects.all()
    if (jokes.count() > 0):
        randIndx = randint(0, jokes.count()-1)
        joke = jokes[randIndx].joke_text
    else:
        joke = "No jokes found :("
    return joke

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
        <h2>Here, enjoy a randomly chosen lame joke:</h2>
        <p>%s</p>
        <p>I can see you... Your current public IP address is: %s</p>
        <p>The current date/time is: %s</p>
    </body>
    </html>
    """ % (count.views, getRandomJoke(), ip, date)
    return HttpResponse(html_doc)