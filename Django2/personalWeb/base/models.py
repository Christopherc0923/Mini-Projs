from django.db import models

# Create your models here.
class Project(models.Model):
    # Django model fields
    title = models.CharField(max_length = 100)
    description = models.CharField(max_length = 250)
    image = models.ImageField(upload_to ='media/')
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title

class Publication(models.Model):
    # Django model fields
    title = models.CharField(max_length = 250)
    description = models.TextField()
    image = models.ImageField(upload_to ='media/')
    url = models.URLField(blank = True)
    
    # Functions that displays title on the admin page
    def __str__(self):
        return self.title