from django import forms
from .models import publicacion, libro,autor

class publicacion_form(forms.ModelForm):
    class Meta:
        model = publicacion
        fields = ['libro','Descripcion','imagen_libro','intercambio','celular']
        labels = {
            'libro' : "libro que desea intercambiar",
            'Descripcion' : "Describa el estado del libro",
            'imagen_libro' : 'Seleccione una imagen del libro',
            'intercambio' : 'por que libro u otro material desea intercambiar',
            'celular' : 'inserte el celular de contacto'
        }

class crear_libro(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo','año_publicacion','autor','categoria']
        labels = {
            'titulo' : 'Escriba el titulo del libro',
            'año_publicacion': 'seleccione el año de publicacion',
            'autor' : 'seleccione al autor',
            'categoria' : 'seleccione la categoria'
        }

class crear_autor(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['nombre','apellido']
        labels = {
            'nombre' : 'escriba el nombre del autor',
            'apellido': 'escriba el apellido del autor'
        }