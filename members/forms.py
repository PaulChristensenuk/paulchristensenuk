from django import forms
from django.core.exceptions import ValidationError



class NameForm(forms.Form):
    name = forms.CharField(
        required=True,
        initial="Name",
        help_text="Write your name here.."  
    )

    def clean_data(self):
        data = self.cleaned_data['name']

        if not str(data).isalpha():
            raise ValidationError('Please enter only letters')
        
        return data





