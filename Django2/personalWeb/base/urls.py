from django.urls import path
from . import views

app_name = "base"

urlpatterns = [
    path('', views.home, name="home"),
    path('adminPage/', views.adminPage, name='adminPage'),
    path('contact/', views.contact, name="contact"),
    path('resume/', views.resume, name="resume"),
    path('ibm/', views.ibm, name="ibm"),
    path('publication/', views.publication, name="publication"),
    #path('room/', views.room, name="room"),

]

