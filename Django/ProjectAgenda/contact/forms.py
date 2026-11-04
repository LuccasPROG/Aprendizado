from django import forms
from django.core.exceptions import ValidationError

from . import models

class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'placeholder': 'Escreva Aqui',
            'help_text' : 'Texto de Ajuda para seu usuário',
        })


    class Meta:
        model = models.Contact
        fields= (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            )

    # def clean(self) :
    #     cleaned_data = self.cleaned_data

    #     self.add_error( 
    #         'first_name',
    #         ValidationError(
    #             'Mensagem de ERROR',
    #             code='invalid'
    #         )
    #     )

    #     return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Não digite ABC',
                    code='invalid'
                )
            )

        return first_name