from django.urls import path
from . import views

urlpatterns = [
	path('',views.GovernmentView.as_view(), name='government-schemes'),
]
