from .models import Idea
from django import forms
from datetime import date


class AddIdea(forms.ModelForm):
    CHOICES = [
        ('High', 'High'),
        ('Mid', 'Mid'),
        ('Low', 'Low')
    ]
    priority = forms.ChoiceField(choices=CHOICES)

    dateAdded = forms.DateField(initial=date.today, widget=forms.HiddenInput())

    class Meta:
        model = Idea
        fields = ['title', 'content', 'dateAdded', 'priority', 'status']
