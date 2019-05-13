from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.get_tasks, name='get_tasks'),
    path('tasks/add/', views.add_task, name='add_task'),
    path('about/', views.about, name='about'),
    path('tasks/<int:id>/edit', views.edit_task, name='edit_task'),
    path('tasks/<int:id>/delete', views.delete_task, name='delete_task')
]