from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('about/', views.About.as_view(), name="about"), 
    path('user/', views.User.as_view(), name="user"), 
    path('rating/create', views.Rating.as_view(), name="rating"), 
    path('requests/', views.Requests.as_view(), name="requests"),   
    path('contacts/', views.Contacts.as_view(), name="contacts"),
]

#Still need to add CRUD routes for ratings & user info 