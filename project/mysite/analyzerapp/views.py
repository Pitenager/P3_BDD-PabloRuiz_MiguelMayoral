# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .text_analyzer.text_analyzer import *
from .forms import IndexForm
from django import forms

def get_text(request):
    if request.method == 'POST':

        form = IndexForm(request.POST)
        form2 = IndexForm()

        if form.is_valid():
            my_text = form.cleaned_data['my_text']
            text_analyzed = TextAnalyzer.run(my_text)
            print(text_analyzed)
            return render(request, 'index.html', {'form':form2,'mytext': text_analyzed})

    else:
        form = IndexForm()

    return render(request, 'index.html',{'form':form})