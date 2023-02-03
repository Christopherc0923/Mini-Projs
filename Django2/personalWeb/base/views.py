from django.shortcuts import render
from .models import Project, Publication


# Create your views here.
def home(request):
    projects = Project.objects.all()
    return render(request, 'base/home.html', {'projects': projects})

def publication(request):
    publications = Publication.objects.all()
    return render(request, 'base/publication.html', {'publications': publications})

def contact(request):
    return render(request, 'base/contact.html')

def resume(request):
    return render(request, 'base/resume.html')

def ibm(request):
    return render(request, 'base/IBMppt.html')

# Admin
from django.urls import reverse
from django.shortcuts import redirect

def adminPage(request):
    admin_url = reverse('admin:index')
    return redirect(admin_url)