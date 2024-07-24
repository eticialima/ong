from django import forms
from .models import MeetingRequest

class MeetingRequestForm(forms.ModelForm):
    class Meta:
        model = MeetingRequest
        fields = ['subject', 'description']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MeetingRequestForm, self).__init__(*args, **kwargs) 
        for field_name, field in self.fields.items():
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'
             