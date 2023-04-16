from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, Textarea
from django.utils.translation import gettext_lazy as _

from .models import Message, Profile


class UserRegisterForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": 'form-control',
                'name': 'password1',
                "placeholder": 'Enter password'
            }
        ),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": 'form-control',
                'name': 'password2',
                "placeholder": 'Re-Enter password'
            }
        ),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": 'form-control',
                'name': 'username',
                "placeholder": 'Enter Username'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": 'form-control',
                'email': 'email',
                "placeholder": 'Enter email'
            }
        )
    )


class LoginForm(AuthenticationForm):
    username = UsernameField(
            widget=forms.TextInput(
                attrs={
                    'autofocus': True,
                    "class": 'mb-0',
                    'name': 'username',
                    "placeholder": 'Enter Username'
                }
            )
        )

    password = forms.CharField(
            label=_("Password"),
            strip=False,
            widget=forms.PasswordInput(
                attrs={
                    "autocomplete": "password",
                    "class": 'mb-0',
                    "name": 'password',
                    "placeholder": 'Enter password'

                }
            )
        )


Product_quantity_choices = [(i, str(i)) for i in range(1, 100)]


class CartProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=Product_quantity_choices,
        coerce=int
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )


class ContactUsForm(ModelForm):

    class Meta:
        model = Message
        fields = {'user', 'email', 'subject', 'message'}
        widgets ={
            'user': TextInput(attrs={"placeholder": 'Your Name', 'id': 'name', "class": "form-control"}),
            'email': TextInput(attrs={"placeholder": "Your Email", 'id': 'email', "class": "form-control"}),
            'subject': TextInput(attrs={"placeholder": "Subject", 'id': 'subject', "class": "form-control"}),
            'message': Textarea(attrs={"placeholder": "Your message", 'id': 'message', "class": "form-control"}),
            'slug': TextInput(attrs={'required': False, 'hidden': True, 'id': 'slug', 'value': ''})
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = {'user', 'email', 'name', 'image'}


