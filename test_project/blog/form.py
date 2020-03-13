from django import forms
from .models import StudentDetails

class Student_details(forms.ModelForm):
    class Meta:
        model=StudentDetails
        fields={}