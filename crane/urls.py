from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('gallery/', views.typo, name="typo"),
    path('typo/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    # path('projects/', views.projects, name="projects"),
]
