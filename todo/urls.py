from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.task_list, name='task_list'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('register/', views.register_view, name='register'),

    # Auth routes
    path('login/', auth_views.LoginView.as_view(template_name='todo/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
]
