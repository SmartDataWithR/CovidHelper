from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True, label='Your message', initial='Please return to me via: my@email.com')
