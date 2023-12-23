from django.forms import ModelForm
from django import forms
from .models import Student

class StudentForm(ModelForm):
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Student
        fiels = "__all__"