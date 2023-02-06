from django.contrib import admin

# Register your models here.
from .models import Project, Publication, Skill, ContactForm
admin.site.register(Project)
admin.site.register(Publication)
admin.site.register(Skill)
admin.site.register(ContactForm)