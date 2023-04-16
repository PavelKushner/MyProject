from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _


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


class ContactUsForm(forms.Form):
    name = forms.CharField(label="Your Name", widget=forms.TextInput(
        attrs={"placeholder": 'Your Name', "class": "form-control"}))
    email = forms.EmailField(label="Your Email", widget=forms.TextInput(
        attrs={"placeholder": "Your Email", "class": "form-control"}))
    subject = forms.CharField(widget=forms.TextInput(
        attrs={"placeholder": "Subject", "class": "form-control"}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={"placeholder": "Your message", "class": "form-control"}))
