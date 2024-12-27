from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug, Hours
from .forms import DrugModelForm, HourModelForm
from django.urls import reverse_lazy

def home_view(request):
    if request.user.is_authenticated:
        total_remedios = Drug.objects.all().filter(user=request.user).count()
    else:
        total_remedios = 0
    return render(request, 'home.html', {'total_remedios': total_remedios})


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
    
## HORARIOS

class HoursCreateView(LoginRequiredMixin, CreateView):
    model = Hours
    form_class = HourModelForm
    template_name = 'hours_createview.html'
    login_url = ('login')

    def get_success_url(self):
        return reverse_lazy('drug_listview')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class HoursListView(LoginRequiredMixin, ListView):
    model = Hours
    template_name = 'hours_listview.html'
    context_object_name = 'horarios'
    login_url = ('login')

    def get_queryset(self):
        return Hours.objects.all().filter(user=self.request.user)
    

    


