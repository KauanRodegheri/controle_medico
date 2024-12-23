from django import forms
from .models import Drug


class DrugModelForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = [item.name for item in Drug._meta.fields]
        