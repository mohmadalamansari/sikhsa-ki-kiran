from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from .models import Agriculture, Training, Complain

# for function views import below line of code
# from django.contrib.auth.decorators import login_required
# @login_required 

# for generic view login_required import below mixin
from django.contrib.auth.mixins import LoginRequiredMixin

class AgricultureList(ListView):
    model = Agriculture

class SchemeDetail(LoginRequiredMixin, DetailView):
    model = Agriculture

# def index(request):
#     return render(request, 'agriculture/index.html',)

class ComplainCreateView(LoginRequiredMixin, CreateView):
    model = Complain
    fields = ['name', 'phone_no', 'complain']
    template_name = 'agriculture/index.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TrainingVideos(LoginRequiredMixin, ListView):
    model = Training
    template_name = 'agriculture/training_videos.html'  # Specify your template for training videos
    context_object_name = 'videos'  # This will be the context variable in the template

    def get_queryset(self):
        # You can customize this method to filter the training videos if needed
        return super().get_queryset()  # This will return all Training objects