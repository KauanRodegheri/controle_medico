from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug
from .forms import DrugModelForm
from django.urls import reverse_lazy

def home_view(request):
    return render(request, 'home.html')


class DrugCreateView(LoginRequiredMixin, CreateView):
    model = Drug
    form_class = DrugModelForm
    template_name = 'drug_createview.html'
    login_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('home_view')
    
class DrugListView(LoginRequiredMixin, ListView):
    model = Drug
    template_name = 'drug_listview.html'
    context_object_name = 'druglist'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Drug.objects.all().filter(user=self.request.user)
    


