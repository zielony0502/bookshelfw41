from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from movies.models import Director


class AddMovieView(View):
    def get(self, request):
        return render(request, 'movies/add_movie.html')


class AddDirectorView(View):
    def get(self, request):
        return render(request, 'movies/add_director.html')

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Director.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponseRedirect(reverse('dodaj_rezysera'))
