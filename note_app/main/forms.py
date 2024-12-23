from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms
from django.forms.widgets import PasswordInput, TextInput

from . import models

class CreateNote(forms.ModelForm):
    class Meta:
        model = models.Note
        fields = ['title','content']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    ## Vulnerability:
    ## Password is exposed as in plaintext within HTML.
    ## How to fix:
    ## Replace TextInput() to PasswordInput()
    password = forms.CharField(widget=TextInput())