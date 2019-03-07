

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def validate_unique_user(error_message, **criteria):
    existent_user = User.objects.filter(**criteria)

    if existent_user:
        raise forms.ValidationError(error_message)


class AuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput({
        'class': 'form-control',
        'placeholder': 'user name',
        })
        )
    password = forms.CharField(label="password", widget=forms.PasswordInput({
        'class': 'form-control',
        'placeholder': 'password',
        })
        )


class SignupForm(forms.Form):
    username = forms.CharField(max_length=10, widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'first name',
                })
            )
    first_name = forms.CharField(
            max_length=100,
            widget=forms.TextInput({
                'class': ' form-control',
                'placeholder': 'first name'
                })
            )
    last_name = forms.CharField(
            max_length=200,
            widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'last name'
                })
            )
    email = forms.CharField(
            max_length=200,
            widget=forms.TextInput({
                'class': 'form-control',
                'placeholder': 'last name'
                })
            )
    password = forms.CharField(
            min_length=6, max_length=10,
            widget=forms.PasswordInput({
                'class': 'form-control',
                'placeholder': 'password'
                })
            )

    repeat_password = forms.CharField(
            min_length=6, max_length=10,
            widget=forms.PasswordInput({
                'class': 'form-control',
                'placeholder': 'repeat password'
                })
            )

    def clean_username(self):
        username = self.cleaned_data['username']

        validate_unique_user(
                error_message='* username already in use',
                username=username)
        return username

    def clean_email(self):
        email = self.cleaned_data['email']

        validate_unique_user(
            error_message='* email already in use',
                email=email
                )
        return email

    def clean_repeat_password(self):
        password1 = self.cleaned_data['password']
        password2 = self.cleaned_data['repeat_password']

        if password1 != password2:
            raise forms.validationerror('* password did not match')

        return password1
