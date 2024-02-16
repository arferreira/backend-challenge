from django.urls import path, include
from . import views
'''Colocar o ponto, refere-se ao próprio diretório'''

urlpatterns = [
    path('', views.task_pending_list, name='task_pending_list'),
    path('<int:task_id>/completed/', views.completed_task, name='completed_task'),
    path('<int:task_id>/delete/', views.delete_task, name='delete_task'),
    path('<int:task_id>/postpone/', views.postpone_task, name='postpone_task'),
    path('<int:task_id>/edit/', views.edit_task, name='edit_task'),
    path('completed/', views.task_completed_list, name='task_completed_list'),
    path('postpone/', views.postpone_task_list, name='postpone_task_list'),
    path('<int:task_id>/move_for_task/', views.move_for_task, name='move_for_task'),
]
