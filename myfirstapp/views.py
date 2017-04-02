from django.shortcuts import render
from django.http import HttpResponse
from .models import ViewCount
from .models import Joke
from random import randint
import time
from ipware.ip import get_ip #installed from: sudo pip install django-ipware

#-----------------------------------------------------------------
#   Fetch a random lame programming joke from the database
#-----------------------------------------------------------------
def getRandomJoke():
    jokes = Joke.objects.all()
    if (jokes.count() > 0):
        randIndx = randint(0, jokes.count()-1)
        joke = jokes[randIndx].joke_text
    else:
        joke = "No jokes found :("
    return joke

#---------------------------------------------------------------------
#
#   Generate dynamic content and return HTTPResponse for myfirstapp 
#   homepage/index.
#
#---------------------------------------------------------------------
def index(request):
    # increment and update page view count fo the current URL
    count, countCreated = ViewCount.objects.get_or_create(url_path=request.path)
    count.views += 1
    count.save()
    
    ip = get_ip(request)
    date = time.strftime("%c")
    
    # Build the html document
    html_doc = """
    <!DOCTYPE html>
    <html>
    <head>
    <style>
        body
        {
            font-family: Arial;
            max-width: 900px;
            margin: auto;
        }
        h1
        {
            text-align: center;
        }
        .joke-wrap
        {
            padding: 5px 12px;
            padding-bottom: 35px;
            background: #eee;
            border-radius: 7px;
        }
        .joke, .note
        {
            max-width: 650px;
            margin: auto;
        }
        .joke
        {
            font-size: 16px;
            line-height: 1.55em;
            margin-bottom: 20px;
        }
        .note
        {
            font-size: 14px;
        }
    </style>
    </head>
    <body>
        <h1>Welcome! You are visitor #%s!</h1>
        <div class="joke-wrap">
            <h2>Here, enjoy a randomly chosen lame joke:</h2>
            <p class="joke">%s</p>
            <p class="note"><i>Note: refreshing this page will most likely generate a new joke.</i></p>
        </div>
        <p>I can see you... Your IP address is: %s</p>
        <p>The current date/time is: %s</p>
    </body>
    </html>
    """ % (count.views, getRandomJoke(), ip, date)
    
    return HttpResponse(html_doc)