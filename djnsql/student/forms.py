from django import forms

class Registraion(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()