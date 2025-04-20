from django.urls import path
from . import views

urlpatterns = [
	path('',views.ComplainCreateView.as_view(),name ='agriculture'),
	path('training/', views.TrainingVideos.as_view(), name= 'training'),
    path('schemes/', views.AgricultureList.as_view(), name='schemes-list'),
    path('schemes/<int:pk>/', views.SchemeDetail.as_view(), name='scheme-detail')
    ]