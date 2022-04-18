from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('about/' views.About.as_view(), name="about"), 
    path('')
]