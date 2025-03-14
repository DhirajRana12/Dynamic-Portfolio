from django.shortcuts import render
from .models import Projet, Skill, AboutMe

# Create your views here.
def home(request):
    aboutme = AboutMe.objects.first()
    projects = Projet.objects.all()
    skills = Skill.objects.all()
    return render(request, 'portfolio/home.html',{'aboutme': aboutme,'projects': projects, 'skills': skills})

def contact(request):  # Add this function
    return render(request, 'portfolio/contact.html')