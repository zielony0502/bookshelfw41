from django import forms

class AddPublisherForm(forms.Form):
    name = forms.CharField(max_length = 5, label='Nazwa')
    year = forms.IntegerField(label='rok')

