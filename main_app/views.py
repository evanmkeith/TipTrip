from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Landing(TemplateView):
    template_name = 'landing.html'

class About(TemplateView):
    template_name = 'about.html'

class User(TemplateView):
    template_name = 'user.html'

class Rating(TemplateView):
    template_name = 'rating.html'

class Requests(TemplateView):
    template_name = 'requests.html'

class Contacts(TemplateView):
    template_name = 'contacts.html'
