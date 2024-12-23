from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug
from .forms import DrugModelForm
from django.urls import reverse_lazy

def home_view(request):
    return render(request, 'home.html')


class DrugCreateView(CreateView, LoginRequiredMixin):
    model = Drug
    form_class = DrugModelForm
    template_name = 'drug_createview.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home_view')


