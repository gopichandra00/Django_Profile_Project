from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import CreateUserForms, PrfileForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from.decorators import unauthenticated_users


# Create your views here.
@login_required(login_url='login')
def index(request):
    return render(request, 'Profileapp/home.html')
@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        form  = ProfileForm(request.POST,request.FILES, instance=user)
        if form is_valid():
            form.save()
            username = request.user.username
            messages.success(request,f'{username}, Your profile is updated.')
            return redirect('/')
    else:
        form = PrfileForm(instance = request.user.profile)
    context = {'form':form}
    return render(request, 'Profileapp/profile.html')
@unauthenticated_users
def login_user(request):


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.info(request, f'{username}, You are logged in.')
            return redirect("/")
        else:
            messages.info(request, f'{username}, Wrong password or username.')
            return redirect('login')
    return render(request, 'Profileapp/login_page.html')
@unauthenticated_users 
def register_user(request):
    form = CreateUserForms()

    if request.method == 'POST':
        form = CreateUserForms(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            redirect('login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials.')
            return render(request, 'Profileapp/register_page.html', context)

    context={'form':form }
    return render(request, 'Profileapp/register_page.html', context)
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    messages.info(request, 'You logged out successfully')
    return redirect('login')