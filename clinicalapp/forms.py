from django import forms
from clinicalapp.models import patient ,ClinicalData


class PatientForm(forms.ModelForm):
    class Meta:
        model=patient
        fields='__all__'


class ClinicalDataForms(forms.ModelForm):
    class Meta:
        model=ClinicalData
        fields='__all__'