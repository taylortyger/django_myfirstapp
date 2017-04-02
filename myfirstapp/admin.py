from django.contrib import admin
from .models import ViewCount
from .models import Joke

# Register your models here.
admin.site.register(ViewCount)
admin.site.register(Joke)