from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View

from accounts.forms import RegisterUserForm


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
