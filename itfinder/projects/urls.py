from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='projects'),
    path('project-object/<slug:project_slug>/', views.project, name='project'),
    path('create-project/', views.createProject, name="create-project"),
    path('update-project/<slug:slug>', views.updateProject, name="update-project"),
    path('delete-project/<slug:slug>', views.deleteProject, name="delete-project"),
    path('tag/<slug:tag_slug>', views.projects_by_tag, name="tag"),
]