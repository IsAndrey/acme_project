from django import forms
from .models import Birthday


class BirthdayForm(forms.ModelForm):
    '''Форма для ввода дня рождения'''

    class Meta:
        model = Birthday
        fields = '__all__'
        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }

        def clean_first_name(self):
            first_name = self.cleaned_data['first_name']
            return first_name.split()[0]
