from django import forms


class AddDirectorForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class AddCompanyForm(forms.Form):
    name = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)
