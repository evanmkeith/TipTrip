from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# user @method_decorator(login_required, name='dispatch') for all paths you want tp auth protect

# Create your views here.
class Landing(TemplateView):
    template_name = 'landing.html'

class About(TemplateView):
    template_name = 'about.html'

#@login_required
class User(TemplateView):
    template_name = 'user.html'

class Rating(TemplateView):
    template_name = 'rating.html'

class Requests(TemplateView):
    template_name = 'requests.html'

class Contacts(TemplateView):
    template_name = 'contacts.html'

def signup_view(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            print("Hello there, ", user.username)
            return HttpResponseRedirect('/user/'+str(user))
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def logout_view(request): 
    logout(request)
    return HttpResponseRedirect('/')

def login_view(request): 
    if request.method == 'POST': 
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/'+username)
                else: 
                    print('The account has been disabled.')
                    return render(request, 'login.html', {'form': form})
            else: 
                print('The username and/or password is incorrect.')
                return render(request, 'login.html', {'form': form})
        else: 
            return render(request, 'signup.html', {'form': form})
    else: 
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})