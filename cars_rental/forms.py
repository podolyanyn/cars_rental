from django.db import models
from .models import InvestorContract
from django import forms
from django.forms import NumberInput

class yourForm(forms.ModelForm):
    last_month_percentage = forms.FloatField(
        initial = 1.111,
    )
    class Meta:
        model = InvestorContract
        fields = ('last_month_percentage',)
        #localized_fields = ('last_month_percentage',)
        widgets = {
            'last_month_percentage': NumberInput(attrs={'value': 'floatformat:2' }), # помилку не видає, але і не працює
            #'last_month_percentage': NumberInput(attrs={'style':'width:270px', 'min':'0', 'max':'1000', 'step':"0.01",}),
        }