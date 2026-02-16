from django import forms
from .models import PulseUser
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={'placeholder': '20 chars max', 'class': 'form-control-lg'})
    )
    email = forms.EmailField(required=True)

    class Meta:
        model = PulseUser
        fields = ('username', 'email', 'password1', 'password2')
