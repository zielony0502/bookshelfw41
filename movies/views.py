from django.shortcuts import render
from django.views import View


class AddMovieView(View):
    def get(self, request):
        return render(request, 'movies/add_movie.html')