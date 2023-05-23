from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')


