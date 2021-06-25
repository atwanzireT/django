from django import forms
from django.forms.fields import DateField
from django.utils.regex_helper import Choice

CHART_CHOICES = (
    ('#1', 'Bar chart'),
    ('#2', 'Pie chart'),
    ('#3', 'Line chart'),

)
class SalesSearchFrom(forms.Form):
    date_form = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    date_to = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    chart_type = forms.ChoiceField(choices = CHART_CHOICES)