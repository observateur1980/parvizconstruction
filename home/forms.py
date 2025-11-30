# forms.py
from django import forms
from .models import LeadModel


class LeadForm(forms.ModelForm):
    class Meta:
        model = LeadModel
        fields = ['name', 'email', 'phone', 'consultation_types', 'message']
        widgets = {
            'consultation_types': forms.CheckboxSelectMultiple,
            'message': forms.Textarea(attrs={'rows': 4}),
        }
