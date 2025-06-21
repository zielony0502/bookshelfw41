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
        directors = Director.objects.all()
        return render(request, 'movies/add_director.html', {"directors": directors})

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        Director.objects.create(first_name=first_name, last_name=last_name)
        return HttpResponseRedirect(reverse('dodaj_rezysera'))


class DeleteDirectorView(View):
    def get(self, request, pk):
        director = Director.objects.get(pk=pk)
        return render(request, 'movies/delete_director.html', {'director': director})

    def post(self, request, pk):
        if request.POST['choice'] == 'Tak':
            director = Director.objects.get(pk= pk)
            director.delete()
        return HttpResponseRedirect(reverse('dodaj_rezysera'))


class UpdateDirectorView(View):
    def get(self, request, pk):
        director = Director.objects.get(pk=pk)
        return render(request, 'movies/update_director.html', {'director': director})

    def post(self, request, pk):
        if request.POST['choice'] == 'Zapisz':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            director  =Director.objects.get(pk=pk)
            director.first_name = first_name
            director.last_name = last_name
            director.save()
        return HttpResponseRedirect(reverse('dodaj_rezysera'))

