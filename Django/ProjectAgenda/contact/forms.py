from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import   UserCreationForm
from django.contrib. auth.models import User

from . import models

class ContactForm(forms.ModelForm):





    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
                }
            )
        )
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
            'picture',
            )


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


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email',
            'username', 'password1', 'password2'
        )

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Já existe este e-mail', code='invalid')
            )