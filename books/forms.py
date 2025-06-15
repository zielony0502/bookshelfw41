from django import forms

from books.models import Book, Genre

def check_name(value):
    if not 's' in value:
        raise forms.ValidationError("Name must be at least one letter s")



class AddPublisherForm(forms.Form):
    name = forms.CharField(max_length = 100, label='Nazwa', validators=[check_name])
    year = forms.IntegerField(label='rok')

class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"

        widgets = {
            'genres': forms.CheckboxSelectMultiple(),
        }

class AddGenreForm(forms.ModelForm):

    class Meta:
        model = Genre
        fields = "__all__"


class BookSearchForm(forms.Form):
    title = forms.CharField(max_length = 50, label='',
                            widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
                            required=False)


