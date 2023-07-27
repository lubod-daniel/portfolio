from django import forms
from .models import VisitorMessage,testimonial
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput, FileInput
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

"""class testimonialform(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = ['remark', 'picture', 'name', 'position', 'organization']
        widgets = {
            'remark':Textarea(
                attrs={
                    "placeholder": "Type your message",
                     "class":"form-control"
                }
            ),
            'picture':FileInput(
                attrs={
                    "placeholder": "upload a photo",
                     "class":"form-control"
                }
            ),
            'name' : TextInput(
            attrs={
                    
                     "class":"form-control"
                }
            
            ),
            'position' : TextInput(
            attrs={
                    
                     "class":"form-control"
                }
            
            ),
            'organization' : TextInput(
            attrs={
                    
                     "class":"form-control"
                }
            
            ),


        }"""

"""class testimonialform(forms.Form):
    remark=forms.CharField(max_length=300)
    picture=forms.FileField()
    name=forms.CharField(max_length=100)
    position=forms.CharField(max_length=100)
    organization=forms.CharField(max_length=100)"""