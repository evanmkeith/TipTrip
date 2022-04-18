from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing_Page.as_view(), name="landing_page"),

]