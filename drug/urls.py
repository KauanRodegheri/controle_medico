from django.urls import path
from .views import DrugCreateView, DrugListView, HoursCreateView, HoursListView, drug_update_view, drug_delete_view


urlpatterns = [
    path('adicionar/remedios', DrugCreateView.as_view(), name='drug_createview'),
    path('lista/', DrugListView.as_view(), name='drug_listview'),
    path('atualizar/<int:pk>/',drug_update_view, name='drug_updateview'),
    path('deletar/<int:pk>/', drug_delete_view, name='drug_deleteview'),
    # HORARIOS
    path('adicionar/horarios/', HoursCreateView.as_view(), name='hours_createview'),
    path('listar/horarios/', HoursListView.as_view(), name='hours_listview'),
]