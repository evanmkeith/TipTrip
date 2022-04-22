from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('about/', views.About.as_view(), name="about"), 
    path('user/<username>/new', views.Create_Profile, name="create_profile"),
    path('user/<username>', views.profile, name="profile"), 
    path('rating/create', views.Rating.as_view(), name="rating"), 
    path('requests/', views.Requests.as_view(), name="requests"),   
    path('contacts/', views.Contacts.as_view(), name="contacts"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"), 
    path('signup/', views.signup_view, name="signup"), 

]

#Still need to add CRUD routes for ratings & user info 