from django.urls import path
from .views import DrugCreateView, DrugListView, HoursCreateView, HoursListView


urlpatterns = [
    path('adicionar/remedios', DrugCreateView.as_view(), name='drug_createview'),
    path('lista/', DrugListView.as_view(), name='drug_listview'),
    # HORARIOS
    path('adicionar/horarios/', HoursCreateView.as_view(), name='hours_createview'),
    path('listar/horarios/', HoursListView.as_view(), name='hours_listview'),
]