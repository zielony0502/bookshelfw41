from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from movies.models import Director, Company, Movie
from movies.forms import AddDirectorForm, AddCompanyForm, AddMovieForm


class AddMovieView(View):
    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies/add_movie.html', {'movies': movies})


class AddDirectorView(View):
    def get(self, request):
        directors = Director.objects.all()
        return render(request, 'movies/add_director.html', {"directors": directors})

    def post(self, request):
        if request.POST['choice'] == 'Zapisz':
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


class AddCompanyView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'movies/add_company.html', {'companies': companies})

    def post(self, request):
        if request.POST['choice'] == 'Zapisz':
            name = request.POST['name']
            country = request.POST['country']
            Company.objects.create(name=name, country=country)
        return HttpResponseRedirect(reverse('dodaj_wytwornie'))


class DeleteCompanyView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return render(request, 'movies/delete_company.html', {'company': company})

    def post(self, request, pk):
        if request.POST['choice'] == 'Tak':
            company = Company.objects.get(pk=pk)
            company.delete()
        return HttpResponseRedirect(reverse('dodaj_wytwornie'))


class UpdateCompanyView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return render(request, 'movies/update_company.html', {'company': company})

    def post(self, request, pk):
        if request.POST['choice'] == 'Zapisz':
            name = request.POST['name']
            country = request.POST['country']
            company = Company.objects.get(pk=pk)
            company.name = name
            company.country = country
            company.save()
        return HttpResponseRedirect(reverse('dodaj_wytwornie'))


class AddDirectorFormView(View):
    def get(self, request):
        form = AddDirectorForm()
        return render(request, 'movies/add_director_form.html', {'form': form})

    def post(self, request):
        if request.POST['choice'] == 'Zapisz':
            form = AddDirectorForm(request.POST)
            if form.is_valid():
                first_name = form.cleaned_data['first_name']
                last_name = form.cleaned_data['last_name']
                Director.objects.create(first_name=first_name, last_name=last_name)
                return HttpResponseRedirect(reverse('dodaj_rezysera_form'))
        form = AddDirectorForm()
        return render(request, 'movies/add_director_form.html', {'form': form})


class AddCompanyFormView(View):
    def get(self, request):
        form = AddCompanyForm()
        return render(request, 'movies/add_company_form.html', {'form': form})

    def post(self, request):
        if request.POST['choice'] == 'Zapisz':
            form = AddCompanyForm(request.POST)
            if form.is_valid():
                name = form.cleaned_data['name']
                country = form.cleaned_data['country']
                Company.objects.create(name=name, country=country)
                return HttpResponseRedirect(reverse('dodaj_wytwornie_form'))
        form = AddCompanyForm()
        return render(request, 'movies/add_company_form.html', {'form': form})


class AddMovieFormView(View):
    def get(self, request):
        form = AddMovieForm()
        return render(request, 'movies/add_movie_form.html', {'form': form})

    def post(self, request):
        if request.POST['choice'] == 'Zapisz':
            form = AddMovieForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                director = form.cleaned_data['director']
                company = form.cleaned_data['company']
                Movie.objects.create(title=title, director=director, company=company)
                return HttpResponseRedirect(reverse('dodaj_film_form'))
        form = AddMovieForm()
        return render(request, 'movies/add_movie_form.html', {'form': form})
