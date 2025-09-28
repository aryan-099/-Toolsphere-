from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Landing Page
def landing(request):
    return render(request, 'landing.html')

# User Registration
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user_login')  # Redirect to login after successful registration
        else:
            messages.error(request, 'Registration failed. Please try again.')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

# User Login
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')  # Redirect to home page after login
        else:
            messages.error(request, 'Invalid credentials')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# User Logout
def logout(request):
    auth_logout(request)
    return redirect('user_login')

# Home Page (protected)
@login_required(login_url='user_login')
def home(request):
    return render(request, 'appz/index.html')

@login_required(login_url='user_login')
def calculator(request):
    return render(request, 'appz/calculator.html')

@login_required(login_url='user_login')
def bmi(request):
    return render(request, 'appz/bmi.html')

@login_required(login_url='user_login')
def area(request):
    return render(request, 'appz/area.html')

@login_required(login_url='user_login')
def currency(request):
    return render(request, 'appz/currency.html')

@login_required(login_url='user_login')
def length(request):
    return render(request, 'appz/length.html')

@login_required(login_url='user_login')
def volume(request):
    return render(request, 'appz/volume.html')

@login_required(login_url='user_login')
def temperature(request):
    return render(request, 'appz/temperature.html')

@login_required(login_url='user_login')
def time(request):
    return render(request, 'appz/time.html')

@login_required(login_url='user_login')
def speed(request):
    return render(request, 'appz/speed.html')

@login_required(login_url='user_login')
def numeral(request):
    return render(request, 'appz/numeral.html')

@login_required(login_url='user_login')
def homeloan(request):
    return render(request, 'appz/homeloan.html')
