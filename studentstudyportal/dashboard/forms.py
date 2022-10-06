from cProfile import label
from dataclasses import fields
from unittest.util import _MAX_LENGTH
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm


class NotesForm(forms.ModelForm):
    
    class Meta:
        model = Notes
        fields = ("title","description")

class DateInput(forms.DateInput):
    input_type = 'date'

class HomeworkForm(forms.ModelForm):
    
    class Meta:
        model = Homework
        widgets = {'due':DateInput()}
        fields = ("subject","title","description","due","is_finished")


class DashboardForm(forms.Form):
    text = forms.CharField(max_length = 100,label="Enter your search")
    # class Meta:
    #     model = Notes
    #     fields = ("title","description")

#
class Form(forms.ModelForm):
    
    class Meta:
        model = Todo
        # widgets = {'due':DateInput()}
        fields = ("title","is_finished")

class ConversionForm(forms.Form):
    CHOICES = [('length','Length'),('mass','Mass')]
    measurment = forms.ChoiceField(choices= CHOICES , widget = forms.RadioSelect)



class ConversionLengthForm(forms.Form):
    CHOICES = [('yard','Yard'),('foot','Foot')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number' ,'placeholder':'enter the number'}
    ))

    measure1 = forms.CharField(
        label= '',widget = forms.Select(choices = CHOICES)
    )

    measure2 = forms.CharField(
        label= '',widget = forms.Select(choices = CHOICES)
    )


class ConversionMassForm(forms.Form):
    CHOICES = [('pund','Pound'),('kilogram','Kilogram')]
    input = forms.CharField(required=False,label=False,widget=forms.TextInput(
        attrs = {'type':'number' ,'placeholder':'enter the number'}
    ))

    measure1 = forms.CharField(
        label= '',widget = forms.Select(choices = CHOICES)
    )

    measure2 = forms.CharField(
        label= '',widget = forms.Select(choices = CHOICES)
    )



class UserRegistrationForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username','password1','password2']