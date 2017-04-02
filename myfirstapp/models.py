from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ViewCount(models.Model):
    url_path = models.URLField(default='defaultURL')
    views = models.PositiveIntegerField(default=0)