from django.urls import path
from . import views


urlpatterns = [
    path('',views.ProjectListview.as_view(),name='Project_list'),
    path('projet/create',views.ProjectCreateView.as_view(),name='Create_list')

]
