from django.shortcuts import render
from .models import Project, Publication, Skill


# Create your views here.
def home(request):
    projects = Project.objects.all()
    skills = Skill.objects.all().order_by('title')
    context = {'projects': projects, 'skills': skills}
    return render(request, 'base/home.html', context)

def publication(request):
    publications = Publication.objects.all()
    context = {'publications': publications}
    return render(request, 'base/publication.html', context)

def contact(request):
    return render(request, 'base/contact.html')

def resume(request):
    return render(request, 'base/resume.html')

def ibm(request):
    return render(request, 'base/IBMppt.html')

def eid101(request):
    return render(request, 'base/eid101.html')

# Admin
from django.urls import reverse
from django.shortcuts import redirect

def adminPage(request):
    admin_url = reverse('admin:index')
    return redirect(admin_url)