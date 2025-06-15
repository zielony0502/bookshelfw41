from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import RegisterUserForm, LoginForm


# Create your views here.
class RegisterView(View):
    def get(self, request):
        form = RegisterUserForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):

        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('home')
        return render(request, 'add_form.html', {'form': form})


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'add_form.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
        return render(request, 'add_form.html', {'form': form, 'error':'nie prawidłowe dane logowania'})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('home')