from django import forms
from .models import Beheerder, Docent, Student, Verantwoording

class BeheerderForm(forms.ModelForm):
    class Meta:
        model = Beheerder
        fields = ['profile_image', 'name', 'lastname', 'email']

class DocentForm(forms.ModelForm):
    class Meta:
        model = Docent
        fields = ['profile_image', 'name', 'lastname', 'email']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['profile_image', 'name', 'lastname', 'email', 'feedback_field']

class VerantwoordingForm(forms.ModelForm):
    class Meta:
        model = Verantwoording
        fields = ['beoordelaar_1', 'feedback_1', 'feedback_1_niveaus', 'beoordelaar_2', 'feedback_2', 'feedback_2_niveaus', 'beoordelaar_3', 'feedback_3', 'feedback_3_niveaus']