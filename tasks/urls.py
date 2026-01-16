from django.urls import path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.home, name='home'),
    path('status/<int:id>/', views.status_changer, name='status_changer'),
    path('incomplete/tasks', views.incomplete, name='incompleted'),
    path('complete/tasks', views.complete, name='completed'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('add/', views.add_task, name='add_task'),
]

