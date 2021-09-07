from .models import Base
from django.forms import ModelForm, DateInput, NumberInput


class BaseForm(ModelForm):
    class Meta:
        model = Base
        # Which fields will be show
        fields = ['date', 'rate']

        # What values will be input fields have and their names
        widgets = {
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'date'
            }),
            "rate": NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'rate'
            }),
        }
