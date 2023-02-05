from django.shortcuts import render

# Create your views here.
def utube(request):
    return render(request, 'utube/home.html')
