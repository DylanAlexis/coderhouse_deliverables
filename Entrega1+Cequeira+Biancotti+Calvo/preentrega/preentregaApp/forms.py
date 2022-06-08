from django import forms
import uuid

class UpdateForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    email = forms.EmailField()