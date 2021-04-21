from django import forms
from django.forms import ModelForm
from .models import *

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class VisitsForm(forms.ModelForm):
    class Meta:
        model = Visits
        fields = '__all__'
