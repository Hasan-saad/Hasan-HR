from django import forms
from .models import Personal, Vacation

class AddEmploey(forms.ModelForm):
    class Meta:
        model = Personal
        fields = '__all__'
        exclude = [ 'user' ]
class AddVacation(forms.ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'
        exclude = [ 'name' ]

