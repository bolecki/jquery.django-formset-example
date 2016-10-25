from django import forms
from .models import Block, Tenant
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div

class BlockForm(forms.ModelForm):
    #description = forms.CharField(label='Description', max_length=255)
    class Meta:
    	model = Block
    	fields = '__all__'


class TenantForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
    	Div('name', style="color: blue;", title="Explication title"),
    	Div('unit', style="color: green;", title="Explication title2")
    )

    class Meta:
    	model = Tenant
    	fields = '__all__'