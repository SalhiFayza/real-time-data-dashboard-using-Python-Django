from django import forms

class NameForm(forms.Form):
    temp = forms.CharField(label='Your name', max_length=100)
