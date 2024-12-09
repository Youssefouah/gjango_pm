from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProjectListview.as_view(),name='Project_list'),
    path('projet/create',views.ProjectCreateView.as_view(),name='Create_list'),
    path('projet/edit/<int:pk>',views.ProjectUpdateView.as_view(),name='Update_list'),
    path('projet/delete/<int:pk>',views.ProjectDelteView.as_view(),name='Delete_list'),
    path('task/create',views.TaskView.as_view(),name='Create_task'),
    path('task/edit/<int:pk>',views.UpdateTaskView.as_view(),name='Update_task'),
    path('task/delete/<int:pk>',views.DeleteTaskView.as_view(),name='Delete_task'),
    

]
