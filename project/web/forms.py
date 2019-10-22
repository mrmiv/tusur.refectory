from django import forms

class user_form(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)