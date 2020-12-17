from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tasks/', views.tasks, name='tasks'),
    path('update/<str:pk>/', views.update_task, name='update'),
    path('delete/<str:pk>/', views.delete_task, name='delete'),
    path('add_category/', views.add_category, name='category'),
    path('update_category/<str:pk>/', views.update_category, name='update-category'),
    path('delete_category/<str:pk>/', views.delete_category, name='delete-category'),
    path('category/<str:cat>/', views.category, name='categories'),
]