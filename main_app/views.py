from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.
class Landing_Page(TemplateView):
    template_name = 'landing_page.html'