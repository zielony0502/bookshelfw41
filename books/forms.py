from django import forms

from books.models import Book


class AddPublisherForm(forms.Form):
    name = forms.CharField(max_length = 100, label='Nazwa')
    year = forms.IntegerField(label='rok')

class AddBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = "__all__"

