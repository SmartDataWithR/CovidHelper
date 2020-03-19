from django import forms

class SearchForm(forms.Form):
    zip_city = forms.CharField(label='Zip Code / City')