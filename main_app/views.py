from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from .models import Profile, Rating, Request
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django import forms
from django.urls import reverse

# user @method_decorator(login_required, name='dispatch') for all paths you want tp auth protect

# Create your views here.
class Landing(TemplateView):
    template_name = 'landing.html'

class About(TemplateView):
    template_name = 'about.html'

class Profile_Form(forms.ModelForm): 
    class Meta: 
        model=Profile
        fields = ['name', 'image_link', 'phone_number', 'zip_code', 'vehicle_type', 'vehicle_make', 'vehicle_model', 'num_seats', 'fee', 'bio']

def Create_Profile(request, pk): 
    if request.method == 'POST': 
        form = Profile_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            image_link = form.cleaned_data['image_link']
            phone_number = form.cleaned_data['phone_number']
            zip_code = form.cleaned_data['zip_code']
            vehicle_type = form.cleaned_data['vehicle_type']
            vehicle_make = form.cleaned_data['vehicle_make']
            vehicle_model = form.cleaned_data['vehicle_model']
            num_seats = form.cleaned_data['num_seats']
            fee = form.cleaned_data['fee']
            bio = form.cleaned_data['bio']
            Profile.objects.create(user=User.objects.get(pk=pk), name=name, image_link=image_link, phone_number=phone_number,zip_code=zip_code, vehicle_type=vehicle_type, vehicle_make=vehicle_make, vehicle_model=vehicle_model, num_seats=num_seats, fee=fee, bio=bio)
            return HttpResponseRedirect('/user/'+str(pk))
        else:
            return render(request, 'create_profile.html', {'form': form})
    else: 
        form=Profile_Form()
        return render(request, 'create_profile.html', {'form': form})

class Edit_Profile(UpdateView): 
    model = Profile
    fields = ['name', 'image_link', 'phone_number', 'zip_code', 'vehicle_type', 'vehicle_make', 'vehicle_model', 'num_seats', 'fee', 'bio']
    template_name = 'edit_profile.html'

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.object.pk})

class Delete_Profile(DeleteView):
    model = User
    template_name = 'user_delete_confirmation.html'
    success_url = "/"

#@login_required
def profile(request, pk):
    user = User.objects.get(pk=pk)
    user_profile = Profile.objects.get(user=user)

    return render(request, 'profile.html', {'user': user, 'user_profile': user_profile})

class Rating(TemplateView):
    template_name = 'rating.html'

class Requests(TemplateView):
    template_name = 'requests.html'

class Contacts(TemplateView):
    model = Profile
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone_number = self.request.GET.get("phone_number")
        if phone_number != None:
            context["contacts"] = Profile.objects.filter(phone_number__icontains=phone_number)
            context["header"] = f'Searching for {phone_number}'
        return context

def signup_view(request): 
    if request.method == 'POST': 
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            login(request, user)
            print("Hello there, ", user.username)
            return HttpResponseRedirect('/user/'+str(user.id)+'/new')
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
                    return HttpResponseRedirect('/user/'+str(user.id))
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

