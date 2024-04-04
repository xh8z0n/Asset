from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .urls import *
from django.contrib.auth import authenticate, login


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True) 

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ('email',) 


def home(request):
    return render(request, 'home.html')

def courses(request):
    return render(request, 'courses.html')

def courses_html(request):
    return render(request, 'courses.html')

def index(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def profile_view(request):
    # Add logic to fetch user profile data if needed
    return render(request, 'profile_info.html')

def reset_view(request):
    # Add logic to fetch user profile data if needed
    return render(request, 'password_reset.html')


def custom_logout(request):
    logout(request)
    # Redirect to the login page after logout
    return redirect('custom_login')  





class CustomLoginView(View):
    def get(self, request):
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Assuming 'home' is the name of your homepage URL pattern
        else:
            # Return an 'invalid login' error message.
            error_message = "Invalid username or password"
            return render(request, 'accounts/login.html', {'error_message': error_message})



class CustomSignupView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            if User.objects.filter(username=username).exists():
                form.add_error('username', 'This username is already taken.')
                return render(request, 'accounts/register.html', {'form': form})
            if User.objects.filter(email=email).exists():
                form.add_error('email', 'This email address is already in use.')
                return render(request, 'accounts/register.html', {'form': form})
            password = form.cleaned_data['password1']
            user = form.save(commit=False)
            user.set_password(password)
            user.save()
            return render(request, 'home.html')
        else:
            return render(request, 'accounts/register.html', {'form': form})
