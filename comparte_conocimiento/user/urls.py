from django.contrib import admin
from django.urls import path
from .views import CreateUserView

urlpatterns = [
    path('Registrarse/', CreateUserView.as_view(), name="registrarse"),
]