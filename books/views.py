from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from books.models import Author, Publisher


class AddAuthorView(View):
    def get(self, request):
        authors = Author.objects.all()
        return render(request, 'books/add_author.html', {'authors': authors})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name  =request.POST['last_name']
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
        return HttpResponseRedirect(reverse('add_author'))


class AddPublisherView(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        return render(request, 'books/add_publisher.html', {'publishers': publishers})

    def post(self, request):
        name = request.POST['name']
        year = request.POST['year']
        Publisher.objects.create(name=name, year=year)
        return HttpResponseRedirect(reverse('add_publisher'))


class DeletePublisher(View):
    def get(self, request, pk):
        publisher = Publisher.objects.get(pk=pk)
        return render(request, 'books/delete_publisher.html', {'publisher': publisher})

    def post(self, request, pk):
        if request.POST['operation'] == 'Tak':
            publisher = Publisher.objects.get(pk=pk)
            publisher.delete()
        return HttpResponseRedirect(reverse('add_publisher'))

