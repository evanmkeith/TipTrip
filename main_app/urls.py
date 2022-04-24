from django.urls import path
from . import views

urlpatterns = [
    path('', views.Landing.as_view(), name="landing"),
    path('about/', views.About.as_view(), name="about"), 
    path('user/<int:pk>/new', views.Create_Profile, name="create_profile"),
    path('user/<int:pk>', views.profile, name="profile"), 
    path('user/<int:pk>/edit', views.Edit_Profile.as_view(), name="edit_profile"),
    path('user/<int:pk>/delete', views.Delete_Profile.as_view(), name="delete_profile"),
    path('user/<int:pk>/rating/<int:id>', views.Create_Rating, name="create_rating"),  
    path('rating/<int:pk>/edit', views.Edit_Rating.as_view(), name="edit_rating"),
    path('rating/<int:pk>/delete', views.Delete_Rating.as_view(), name="delete_rating"),
    path('user/<int:pk>/contacts/', views.Contacts.as_view(), name="contacts"),
    path('user/<int:pk>/contacts/add/<int:id>', views.Add_Contact, name="add_contact"),
    path('user/<int:pk>/contacts/remove/<int:id>', views.Remove_Contact, name="remove_contact"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"), 
    path('signup/', views.signup_view, name="signup"), 
]

#Still need to add CRUD routes for ratings & user info 