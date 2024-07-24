from django import forms
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

class ContactForm(forms.Form):
    name = forms.CharField(label='Nome', required=True)
    sender_email = forms.CharField(label='E-mail', required=True)
    subject = forms.CharField(label='Assunto', required=True)
    message = forms.CharField(label='Mensagem', widget=forms.Textarea, required=True)

    def __init__(self, *args, **kwargs): 
        super(ContactForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-input'

    def send_email(self, form, recipient_list, template_email):
        context = form.cleaned_data
        subject = '{}'.format(context['subject'])
        message = render_to_string(template_email, context)
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list)