from django.urls import path
from .views import registration, task_list, create_task, delete_task, user_login, complete_task, update_task
from .views import TaskGenericApiView, SingleTaskApiView

app_name = 'single'

urlpatterns = [
    path('', task_list, name='task_list'),
    path('registration/', registration, name='registration'),
    path('login/', user_login, name='login'),
    path('create-task/', create_task, name='create_task'),
    path('update_task/<int:task_id>/', update_task, name='update_task'),
    path('complete_task/<int:task_id>/', complete_task, name='complete_task'),
    path('delete-task/<int:task_id>/', delete_task, name='delete_task'),
    path('api/single/<pk>', SingleTaskApiView.as_view(), name='single'),
    path('api/tasks/', TaskGenericApiView.as_view(), name='api_task_list'),
    ]
