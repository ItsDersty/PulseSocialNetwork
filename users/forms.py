from django import forms
from .models import PulseUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = PulseUser
        fields = ('username', 'email', 'password1', 'password2')
