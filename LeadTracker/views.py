from django.shortcuts import render
from .forms import CustomUserCreationForm, LoginForm

def index(request):
    return render(request, 'LeadTracker/index.html')    # This is the path to the index.html file 

def registerPage(request):
    form = CustomUserCreationForm()
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('login')
        context = {'form': form}
        
    return render(request, 'LeadTracker/register.html', context)


