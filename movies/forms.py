from django import forms

from movies.models import Movie


class AddDirectorForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)


class AddCompanyForm(forms.Form):
    name = forms.CharField(max_length=50)
    country = forms.CharField(max_length=50)


class AddMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

