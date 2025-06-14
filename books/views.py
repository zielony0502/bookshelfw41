from django.shortcuts import render
from django.views import View


# Create your views here

class AddBookView(View):
    def get(self, request):
        return render(request, 'books/add_book.html')