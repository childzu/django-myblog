from django import forms
from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(), max_length=512)
    content = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = Post
        fields = ['title', 'content']

class NewCommentForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.Textarea(), max_length=256)

    class Meta:
        model = Comment
        fields = ['email', 'message']