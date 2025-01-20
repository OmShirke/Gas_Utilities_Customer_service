from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer_name', 'email','request_type', 'description']
        widgets = {
            'request_type': forms.Select(),
        }

class ServiceRequestResponseForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['response', 'status']  # Admin can update response and status
        widgets = {
            'response': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }