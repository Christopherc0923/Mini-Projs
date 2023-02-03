from django.db import models

# Create your models here.
class Blogpage(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(max_length=250)

    # Functions that displays title on the admin page
    def __str__(self):
        return self.title