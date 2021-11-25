from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='forgottenEmail', max_length=100)
