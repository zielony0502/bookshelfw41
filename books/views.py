from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse

from books.models import Author


class AddAuthorView(View):
    def get(self, request):
        return render(request, 'books/add_author.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name  =request.POST['last_name']
        Author.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponseRedirect(reverse('add_author'))
