from django import forms
from .models import Birthday
from django.core.exceptions import ValidationError


STATE_HEADERS = {'Адольф Гитлер', 'Бенитто Муссолини', 'Барак Абама',
                 'Джордж Буш', 'Ислам Кримов', 'Владимир Зеленский',
                 'Владимир Путин'}


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
        print(first_name)
        first_name = first_name.split()[0]
        print(first_name)
        return first_name

    def clean(self):
        first_name = self.cleaned_data['first_name']
        second_name = self.cleaned_data['second_name']
        full_name = f'{first_name} {second_name}'
        if full_name in STATE_HEADERS:
            raise ValidationError(
                'Сбор и обработка информации о '
                'государственных руководителях запрещён!'
            )
