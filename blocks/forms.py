from django import forms
from .models import Block

class BlockForm(forms.ModelForm):
    #description = forms.CharField(label='Description', max_length=255)
    class Meta:
    	model = Block
    	fields = '__all__'


class BuildingForm(forms.Form):
    description = forms.CharField(label='Description', max_length=255)
    block = forms.ModelChoiceField(queryset=None)
    address = forms.CharField(label='Address', max_length=255)


class TenantForm(forms.Form):
    building = forms.ModelChoiceField(queryset=None)
    name = forms.CharField(label='Name', max_length=255)
    unit = forms.CharField(max_length=255)
