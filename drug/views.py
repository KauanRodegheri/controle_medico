from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Drug, Hours
from .forms import DrugModelForm, HourModelForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404


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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
class DrugListView(LoginRequiredMixin, ListView):
    model = Drug
    template_name = 'drug_listview.html'
    context_object_name = 'druglist'
    login_url = reverse_lazy('login')

    def get_queryset(self):
        return Drug.objects.all().filter(user=self.request.user)
    

def drug_update_view(request, pk):
    object = get_object_or_404(Drug, pk=pk)
    if request.method == 'POST':
        drugs_forms = DrugModelForm(request.POST, instance=object)
        if drugs_forms.is_valid():
            drugs_forms.save()
            return redirect('drug_listview')
    else:
        drugs_forms = DrugModelForm(instance=object)
    return render(request, 'drug_updateview.html', {'drugs_forms': drugs_forms})
    

def drug_delete_view(request, pk):
    object = get_object_or_404(Drug, pk=pk)
    if request.method == 'POST':
        if object:
            object.delete()
            return redirect('drug_listview')
    return render(request, 'drug_deleteview.html', {'object': object})

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
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class HoursListView(LoginRequiredMixin, ListView):
    model = Hours
    template_name = 'hours_listview.html'
    context_object_name = 'horarios'
    login_url = ('login')

    def get_queryset(self):
        return Hours.objects.all().filter(user=self.request.user)
    


    

    


