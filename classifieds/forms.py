from django import forms

from .models import ClassifiedAd

class ClassifiedAdForm(forms.ModelForm):
    class Meta:
        model = ClassifiedAd
        fields = ['category', 'headline', 'body', 'email']
        labels = {'headline':'', 'body':'', 'email':''}
        widgets = {'body':forms.Textarea(attrs={'cols':80})}
