from django import forms

class DatePickerInput(forms.DateInput):
        input_type = 'date'
        
class TimePickerInput(forms.TimeInput):
        input_type = 'time'

class DateTimePickerInput(forms.DateTimeInput):
        input_type = 'datetime'

class FileInput(forms.FileInput):
        input_type = 'file'