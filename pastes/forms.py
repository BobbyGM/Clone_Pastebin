from django import forms
from .models import Paste


class PasteForm(forms.ModelForm):
    class Meta:
        model = Paste
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }
