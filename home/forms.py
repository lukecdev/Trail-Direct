from django import forms
from .models import Newsletter

class NewsletterForm(forms.Form):
    """
    Form newsletters subsribers 
    """
    class Meta:
        model = Newsletter
        fields = ['name', 'email']