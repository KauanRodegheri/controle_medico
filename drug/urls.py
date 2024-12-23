from django.urls import path
from .views import DrugCreateView


urlpatterns = [
    path('adicionar/', DrugCreateView.as_view(), name='drug_createview'),
  #  path('horarios/', )
]