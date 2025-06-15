from django import forms


class AddPublisherForm(forms.Form):
    name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Wydawnictwo'}))
    year = forms.IntegerField(label='', widget=forms.TextInput(attrs={'placeholder': 'Rok założenia'}))

class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Imię'}))
    last_name = forms.CharField(max_length=50, label='', widget=forms.TextInput(attrs={'placeholder': 'Nazwisko'}))