from django.shortcuts import render, redirect
from .models import Schedule
from .forms import SchedulesModelForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def schedules_create_view(request):
    if request.method == 'POST':
        schedules = SchedulesModelForm(request.POST)
        if schedules.is_valid():
            schedule = schedules.save(commit=False)
            schedule.user = request.user
            schedule.save()
            return redirect('schedules_listview')
    else:
        schedules = SchedulesModelForm()
    return render(request, 'schedules_createview.html', {'schedules': schedules})

@login_required(login_url='login')
def schedules_listview(request):
    schedules = Schedule.objects.all().filter(user=request.user)
    return render(request, 'schedules_listview.html', {'schedules': schedules})
