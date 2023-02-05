from django.urls import path
from . import views

# Assign appname for clarity
app_name = "utube"

urlpatterns = [
    path('', views.utube, name="utube"),
] 