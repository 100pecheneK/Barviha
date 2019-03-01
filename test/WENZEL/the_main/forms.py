from django import forms
from .models import *

class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)