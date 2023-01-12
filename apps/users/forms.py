from django import forms
from django.forms import widgets

from apps.users.models import User


class BaseForm(forms.Form):
    username = forms.CharField(widget=widgets.TextInput(attrs={"placeholder": "Имя пользователя"}))
    password = forms.CharField(widget=widgets.PasswordInput(attrs={"placeholder": "Пароль"}))


class RegistrationForm(BaseForm, forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]


class AuthorizationForm(BaseForm):
    pass
