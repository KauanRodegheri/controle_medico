from django import forms
from .models import Drug, Hours


class DrugModelForm(forms.ModelForm):

    class Meta:
        model = Drug
        fields = ['name']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(DrugModelForm, self).__init__(*args, **kwargs)

    
    def clean_name(self):
        name = self.cleaned_data.get('name')
        print(name)
        print(self.user)
        if Drug.objects.all().filter(user=self.user, name=name).exists():
            self.add_error('name', 'ja existe esse remedio no banco')
        else:
            return name


class HourModelForm(forms.ModelForm):

    class Meta:
        model = Hours
        fields = ['hours', 'drugs']
        widgets = {
            'hours': forms.TimeInput(format='%H:%M:%S', attrs={'type': 'time'})
        }