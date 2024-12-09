from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy,reverse
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProjectListview(LoginRequiredMixin,ListView):
    model = models.Projects
    template_name = 'projects/list.html'
    paginate_by = 3
    def get_queryset(self):
        query_set = super().get_queryset()
        where ={}
        q = self.request.GET.get('q',None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('Project_list')

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = 'projects/update.html'
    #success_url = reverse_lazy('Project_list')
    def get_success_url(self):
        return reverse('Update_list',args=[self.object.id])

class ProjectDelteView(LoginRequiredMixin,DeleteView):
    model = models.Projects
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('Project_list')
     
    
class TaskView(LoginRequiredMixin,CreateView):
    model = models.Tasks
    fields = ['project','description']
    http_method_names =['post']
    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])
    
class UpdateTaskView(LoginRequiredMixin,UpdateView):
    model = models.Tasks
    fields = ['is_completed']
    http_method_names =['post']
    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])

class DeleteTaskView(LoginRequiredMixin,DeleteView):
    model = models.Tasks

    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])
