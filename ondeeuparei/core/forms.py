# coding: utf-8
from django import forms
from ondeeuparei.core.models import Reminder

class ReminderForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    place = forms.CharField(max_length=15)

    class Meta:
        model  = Reminder
        fields = ('title', 'place')