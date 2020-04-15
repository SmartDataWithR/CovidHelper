from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(
        widget=forms.TextInput(attrs={'placeholder': 'Your Email'}), required=True)
    subject = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'What can we do for you?'}), required=True)
    message = forms.CharField(widget=forms.Textarea(
        attrs={'placeholder': 'Your message to us.'}), required=True)
