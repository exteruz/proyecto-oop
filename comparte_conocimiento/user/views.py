from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistroForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

class CreateUserView(CreateView):
    model = User
    form_class = RegistroForm
    template_name = '../templates/registration/user_form.html'
    success_url = reverse_lazy('inicio')

# Create your views here.
