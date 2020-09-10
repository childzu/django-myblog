from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), max_length=512)
    content = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Post
        fields = ['title', 'content']