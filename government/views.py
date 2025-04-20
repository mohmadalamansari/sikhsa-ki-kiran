from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import GovernmentSchemes


class GovernmentView(ListView):
	model = GovernmentSchemes
	template_name = 'government/government.html'

