from django.urls import path
from .views import schedules_create_view, schedules_listview


urlpatterns= [
    path('adicionar/agendamentos/', schedules_create_view, name='schedules_createview'),
    path('listar/agendamentos/', schedules_listview, name='schedules_listview')
]