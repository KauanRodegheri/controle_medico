from django.urls import path
from .views import exams_create_view, exams_list_view


urlpatterns = [
    path('cadastrar/exams/', exams_create_view, name='exams_createview'),
    path('listar/exams/', exams_list_view, name='exams_listview'),
]