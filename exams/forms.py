from django import forms
from .models import Exams


class ExamsModelForm(forms.ModelForm):
    
    class Meta:
        model = Exams
        fields = ['file', 'day']
        widgets = {
            'day': forms.DateInput(format='%D:%M:%Y', attrs={'type': 'date'})
        }