from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):
    name = forms.CharField(max_length=50, required=True, label="Имя")
    email = forms.EmailField(max_length=50, required=True)
    password1 = forms.CharField(
        label="Введите пороль",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Пороль более 5 символов"}),
    )
    password2 = forms.CharField(
        label="Повторите пороль",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Пороль более 5 символов"}),
    )

    class Meta:
        model = CustomUser
        fields = (
            "name",
            "email",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "name",
            "email",
        )


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
