from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from books.forms import AddPublisherForm, AddBookForm
from books.models import Author, Publisher


# Create your views here

class AddAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'books/add_author.html', {'authors': authors})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponseRedirect(reverse('add_author'))

class DeleteAuthorView(View):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        return render(request, 'books/delete_author.html', {'author': author})

    def post(self, request, pk):
        if request.POST['operation'] == 'Tak':
            author = Author.objects.get(pk=pk)
            author.delete()
        return HttpResponseRedirect(reverse('add_author'))

class UpdateAuthorView(View):
    def get(self, request, pk):
        author = Author.objects.get(pk=pk)
        return render(request, 'books/update_author.html', {'author': author})

    def post(self, request, pk):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        author = Author.objects.get(pk=pk)
        author.first_name = first_name
        author.last_name = last_name
        author.save()
        return HttpResponseRedirect(reverse('update_author', args=[pk]))


class AddPublisherView(View):
    def get(self, request):
        form = AddPublisherForm()
        return render(request, 'books/add_form.html', {'form': form})

    def post(self, request):
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            year = form.cleaned_data['year']
            Publisher.objects.create(name=name, year=year)
            return HttpResponseRedirect(reverse('add_publisher'))
        return render(request, 'books/add_form.html', {'form': form})


class AddBookView(View):
    def get(self, request):
        form = AddBookForm()
        return render(request, 'books/add_form.html', {'form': form})

    def post(self, request):
        form = AddBookForm(request.POST)
        if form.is_valid():
            book = form.save()
            return HttpResponseRedirect(reverse('add_book'))
        return render(request, 'books/add_form.html', {'form': form})