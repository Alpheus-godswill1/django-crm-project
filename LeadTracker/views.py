from django.shortcuts import render



def index(request):
    return render(request, 'LeadTracker/index.html')    # This is the path to the index.html file 

