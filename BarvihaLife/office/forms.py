from django.forms import ModelForm
from .models import room

class roomForm(ModelForm):
    class Meta:
        model = room
        fields = ['title', 'title', 'title','description']
        #fields = '__all__'
