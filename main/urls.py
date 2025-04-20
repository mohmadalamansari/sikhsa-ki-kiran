from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main-index'), 
    path('about/', views.about, name='about'),
    path('issues-addressed/', views.issues, name='issues'),
    path('solution/', views.solution, name='solution'),
    path('terms-of-service/', views.terms, name='terms'),
    path('prospective-impact/', views.prospective, name='prospective'),
]