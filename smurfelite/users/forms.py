from django import forms

from .models import Profile


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter username",
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter Email Address",
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Enter Password",
            }
        )
    )
    password_repeat = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control form-control-lg",
                "placeholder": "Confirm Password",
            }
        )
    )


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter First Name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Enter Last Name"})
    )

    class Meta:
        model = Profile
        exclude = ("user", "id")
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Enter a username"}),
            "email": forms.EmailInput(attrs={"placeholder": "Enter an Email Id"}),
        }
