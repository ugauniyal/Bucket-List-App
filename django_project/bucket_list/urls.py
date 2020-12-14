from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tasks/', views.tasks, name='tasks'),
    path('update/<str:pk>/', views.update_task, name='update'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
]