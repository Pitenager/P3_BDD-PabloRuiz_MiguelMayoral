# -*- coding: utf-8 -*-

from django import forms

class IndexForm(forms.Form):
    my_text = forms.CharField(widget=forms.Textarea, label="Text to analyze",max_length=100)