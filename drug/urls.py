from django.urls import path
from .views import DrugCreateView, DrugListView


urlpatterns = [
    path('adicionar/', DrugCreateView.as_view(), name='drug_createview'),
    path('lista/', DrugListView.as_view(), name='drug_listview'),
  #  path('horarios/', )
]