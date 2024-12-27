from django.shortcuts import render, redirect
from .forms import ExamsModelForm
from django.contrib.auth.decorators import login_required
from .models import Exams


@login_required(login_url='login')
def exams_create_view(request):
    if request.method == 'POST':
        exams_form = ExamsModelForm(request.POST, request.FILES)
        if exams_form.is_valid():
            exams = exams_form.save(commit=False)
            exams.user = request.user
            exams.save()
            return redirect('exams_listview')
    else:
        exams_form = ExamsModelForm()
    return render(request, 'exams_createview.html', {'exams_form': exams_form})

@login_required(login_url='login')
def exams_list_view(request):
    exams = Exams.objects.all().filter(user=request.user)
    return render(request, 'exams_listview.html', {'exams': exams})


