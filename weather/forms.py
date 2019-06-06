from django.forms import ModelForm, TextInput
from .models import City, City1
from django import forms


class CityForm(ModelForm):
    class Meta:
        model = City
        model = City1
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder

class Cform(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class' : 'input', 'placeholder' : 'City Name'}),
        } #updates the input class to have the correct Bulma class and placeholder


class FeedbackForm(forms.Form):
    Name = forms.CharField(required = True)
    Email = forms.EmailField(required = True)
    message = forms.CharField(widget = forms.Textarea , required = True)
