from django.shortcuts import render
from django.views.generic import ListView,CreateView
from . import models
from django.urls import reverse_lazy
from . import forms
# Create your views here.


class ProjectListview(ListView):
    model = models.Projects
    template_name = 'projects/list.html'

class ProjectCreateView(CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('Project_list')
    