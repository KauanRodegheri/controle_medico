from django import forms
from .models import Schedule


class SchedulesModelForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['day', 'specialist', 'hospital']
        widgets = {
            'day': forms.DateTimeInput(format='%D:%M:%Y:%H:%M',attrs={'type': 'datetime-local'})
        }