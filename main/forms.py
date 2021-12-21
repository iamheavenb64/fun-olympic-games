from django import forms
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation  



class Changepasswordform(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New password",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'autofocus': True, 'class': 'form-control'}),
    )
    
class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control'})
    )


class PasswordResetConfirm(SetPasswordForm):
    new_password1 = forms.CharField(
        label="New password",
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label="New password confirmation",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
    ) 