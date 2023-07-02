from django import forms
from .models import Guest_book


class GuestForms(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Guest_book
        fields = ['name', 'email_author', 'entry_text']