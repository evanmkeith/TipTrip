from django.contrib import admin
from .models import Profile, Request, Rating

# Register your models here.
admin.site.register(Profile)
admin.site.register(Request)
admin.site.register(Rating)