from django.db import forms

class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label='Логин',