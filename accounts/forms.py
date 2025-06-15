from django import forms
from django.contrib.auth.models import User


class RegisterUserForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        data = super().clean()
        if data['password1'] != data['password2']:
            raise forms.ValidationError("Password mismatch")

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


