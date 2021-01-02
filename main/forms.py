from django import forms
from django.core import validators


def must_be_empty(value):
    if value:
        raise forms.ValidationError('ce champs doit etre vide')

class ContactForm(forms.Form):
    name     = forms.CharField(required = True, max_length=100)
    email    = forms.EmailField(required = True)
    subject  = forms.CharField( max_length=100)
    phone    = forms.CharField(required = True, max_length=16)
    # file     = forms.FileField(required=False)
    message  = forms.CharField(widget=forms.Textarea, required = True)
    honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])


class DevisForm(forms.Form):
    name     = forms.CharField(required = True, max_length=100)
    email    = forms.EmailField(required = True)
    phone    = forms.CharField(required = True, max_length=16)
    # file     = forms.FileField(required=False)
    message  = forms.CharField(widget=forms.Textarea, required = True)
    honeypot = forms.CharField(required=False,  label="leave empty", validators=[must_be_empty])