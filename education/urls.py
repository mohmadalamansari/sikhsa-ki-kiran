from django.urls import path
from . import views
from .views import EducationSubjectList, EducationTopicList, EducationVideoList

urlpatterns = [
    path('', EducationSubjectList.as_view(),name='subject-list'),
    path('<str:subject>/', EducationTopicList.as_view(), name= 'topic-list'),
    path('<str:subject>/<str:topic>/', EducationVideoList.as_view(), name='video-list')
]