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

class EditUserForm(forms.ModelForm):
    bio = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.Textarea(attrs={
        "rows": 4,
        "class": "form-control fs-4"
    })
    )

    class Meta:
        model = PulseUser
        fields = ('bio',)
        labels = {
            'bio': 'Biography',
        }
