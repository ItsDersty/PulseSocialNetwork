from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    content = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.Textarea(attrs={
        "rows": 4,
        "class": "form-control fs-4"
    })
    )

    class Meta:
        model = Post
        fields = ('content',)
