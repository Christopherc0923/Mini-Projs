from django.contrib import admin

# Register your models here.
from .models import Project, Publication
admin.site.register(Project)
admin.site.register(Publication)