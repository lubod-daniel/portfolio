from django import forms
from .models import VisitorMessage
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput
from django.forms import Textarea, TextInput


class VisitorMessageForm(forms.ModelForm):
    class Meta:
        model = VisitorMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name' : TextInput(
            attrs={
                    
                     "class":"form-control"
                }
            
            ),
            'email' : TextInput(
            attrs={
                    
                     "class":"form-control"
                }
            
            ),
            'message':Textarea(
                attrs={
                    "placeholder": "Type your message",
                     "class":"form-control"
                }
            ),

        }