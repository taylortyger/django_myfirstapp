from __future__ import unicode_literals

from django.db import models

# Create your models here.

# stores the number of times a URL has been accessed/viewed
class ViewCount(models.Model):
    url_path = models.URLField(default='defaultURL')
    views = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.url_path

# stores funny CS jokes to display on the homepage
class Joke(models.Model):
    joke_title = models.CharField(max_length=200)
    joke_text = models.CharField(max_length=2000)
    def __str__(self):
        return self.joke_title