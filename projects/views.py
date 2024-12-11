from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from . import models
from django.urls import reverse_lazy,reverse
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.


class ProjectListview(LoginRequiredMixin,ListView):
    model = models.Projects
    template_name = 'projects/list.html'
    paginate_by = 3
    def get_queryset(self):
        query_set = super().get_queryset()
        where ={'user_id':self.request.user}
        q = self.request.GET.get('q',None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


class ProjectCreateView(LoginRequiredMixin,CreateView):
    model = models.Projects
    form_class = forms.ProjectCreateForm
    template_name = 'projects/create.html'
    success_url = reverse_lazy('Project_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProjectUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Projects
    form_class = forms.ProjectUpdateForm
    template_name = 'projects/update.html'
    #success_url = reverse_lazy('Project_list')
    
    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Update_list',args=[self.object.id])

class ProjectDelteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Projects
    template_name = 'projects/delete.html'
    success_url = reverse_lazy('Project_list')
    def test_func(self):
        return self.get_object().user_id == self.request.user.id
    
class TaskView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model = models.Tasks
    fields = ['project','description']
    http_method_names =['post']
    
    def test_func(self):
        project_id = self.request.POST.get('project','')
        return models.Projects.objects.get(pk= project_id).user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])
    
class UpdateTaskView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Tasks
    fields = ['is_completed']
    http_method_names =['post']

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])

class DeleteTaskView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = models.Tasks

    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id

    def get_success_url(self):
        return reverse('Update_list',args=[self.object.project.id])
