from typing import Any
from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    designation=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    department=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    salary=forms.IntegerField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

    def clean(self):
        clean_data=super().clean()
        salary=clean_data.get("salary")
        if salary not in range(50000,10000000):
            error_message="Not in given range.pls enter above 50000"

            self.add_error("salary",error_message)

