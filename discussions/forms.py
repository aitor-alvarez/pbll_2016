# discussions/forms.py
from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'text', 'creator', 'parent_post']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'cols': '100%', 'class': 'form-control content-editor'}),
            'creator': forms.HiddenInput(),
            'parent_post': forms.HiddenInput(), 
        }
        labels = { 'text': 'Message Text...', 'subject': 'Subject line...'}

        
class PostReplyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'text', 'creator', 'parent_post']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 2, 'cols': '100%', 'class': 'form-control discussion-editor'}),
            'subject': forms.TextInput(attrs={'size': '75%'}),
            'creator': forms.HiddenInput(),
            'parent_post': forms.HiddenInput(), 
        }
        labels = { 'text': '', 'subject': 'Subject line:'}

class PostSubthreadReplyForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'text', 'creator', 'parent_post']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 1, 'class': 'form-control '}),
            'subject': forms.HiddenInput(),
            'creator': forms.HiddenInput(),
            'parent_post': forms.HiddenInput(), 
        }
        labels = { 'text': ''}