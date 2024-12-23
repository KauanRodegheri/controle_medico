from django import forms
from .models import Drug


class DrugModelForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = ['name']
