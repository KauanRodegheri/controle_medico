from django import forms
from .models import Drug, Hours


class DrugModelForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = ['name']


class HourModelForm(forms.ModelForm):

    class Meta:
        model = Hours
        fields = ['hours', 'drugs']
        widgets = {
            'hours': forms.TimeInput(format='%H:%M:%S', attrs={'type': 'time'})
        }