from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, LoginForm

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import auth 

def index(request):
    return render(request, 'LeadTracker/index.html')    # This is the path to the index.html file 

def registerPage(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form': form}
        
    return render(request, 'LeadTracker/register.html', context)

def loginPage(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                
                auth.login(request, user)
                # return redirect('index')
    
    context = { 'form': form }
    return render(request, 'LeadTracker/login.html', context)


