"""Forms used in classified ads."""
from django import forms

from .models import ClassifiedAd


class ClassifiedAdForm(forms.ModelForm):
    """A form to fill out a classified ad."""

    class Meta:
        """Fields included in the form."""

        model = ClassifiedAd
        fields = ['category', 'headline', 'body', 'email']
        labels = {'headline': '', 'body': '', 'email': ''}
        widgets = {'body': forms.Textarea(attrs={'cols': 80})}
