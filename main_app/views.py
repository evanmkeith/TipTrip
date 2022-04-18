from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Landing(TemplateView):
    template_name = 'landing.html'

class About(TemplateView):
    template_name = 'about.html'

