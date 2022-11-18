from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        signup_form = CustomUserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        signup_form = CustomUserCreationForm()

    context = {
        'signup_form' : signup_form, 
    }

    return render(request, 'accounts/signup.html', context)


# modal 변경 예정
def login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            auth_login(request, login_form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')

    
    else:
        login_form = AuthenticationForm()

    context = {
        'login_form' : login_form
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    
    auth_logout(request)

    return redirect('articles:index')