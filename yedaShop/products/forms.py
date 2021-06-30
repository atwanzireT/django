from django import forms
from django.utils.regex_helper import Choice



class Submit(forms.Form):
    email = forms.EmailField()