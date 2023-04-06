from django import forms
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
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
        # strip=False,
        # help_text=_("Enter the same password as before, for verification."),
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
