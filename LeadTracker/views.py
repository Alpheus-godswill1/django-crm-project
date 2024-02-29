from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'LeadTracker/index.html')    # This is the path to the index.html file 

