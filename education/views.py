import requests
from django.shortcuts import render
from .models import Subject, Topic, Video
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

class EducationSubjectList(ListView):
    model = Subject
    template_name = 'education/education.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_videos'] = Video.objects.all()[:10]  # You can filter/sort here if needed
        return context

class EducationTopicList(ListView):
    model = Topic

    def get_queryset(self):
        subject = Subject.objects.get(subject_name=self.kwargs['subject'])
        return Topic.objects.filter(subject=subject)

class EducationVideoList(LoginRequiredMixin, ListView):
    model = Video

    def get_queryset(self):
        topic = Topic.objects.get(topic_name=self.kwargs['topic'])
        return Video.objects.filter(topic=topic)

# OPTIONAL: Old experimental view (commented out) kept for reference
# def education(request):
#     topic_tree_url = 'https://www.khanacademy.org/api/v1/topictree?kind=topic'
#     main_data = requests.get(topic_tree_url).json()
#     topic_nodes = list(filter(lambda x: x['render_type'] == 'Domain', main_data['children']))
#     for topic in topic_nodes:
#         topic['topic_subjects'] = list(filter(lambda x: x['curriculum_key'] == '', topic['children']))
#     context = {
#         'topic_nodes': topic_nodes,
#     }
#     return render(request, 'education/education.html', context)
