from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',


        ]
        labels = {
            
            'first_name' : "nombre",
            'last_name': "apellido",
            'username': "nombre de usuario",
            'email':"correo electronico",

        }
