from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('bin/', views.bin_view, name='tasks_bin'),
    path('delete/<int:pk>/', views.delete_task, name='task_delete'),
    path('restore/<int:pk>/', views.restore_task, name='task_restore'),
    path(
        'hard-delete/<int:pk>/',
        views.hard_delete_task,
        name='task_hard_delete',
    ),
    path('empty-bin/', views.empty_bin, name='tasks_empty_bin'),
]
