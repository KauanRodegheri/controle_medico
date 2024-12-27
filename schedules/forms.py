from django import forms
from .models import Schedule


class SchedulesModelForm(forms.ModelForm):

    class Meta:
        model = Schedule
        fields = ['day', 'specialist', 'hospital']
        