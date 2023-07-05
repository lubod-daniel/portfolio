from django import forms
from .models import VisitorMessage

class VisitorMessageForm(forms.ModelForm):
    class Meta:
        model = VisitorMessage
        fields = ['name', 'email', 'message']
