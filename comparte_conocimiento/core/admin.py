from django.contrib import admin
from .models import autor,categoria,libro,publicacion,perfil

admin.site.register(autor)
admin.site.register(categoria)
admin.site.register(libro)
admin.site.register(publicacion)
admin.site.register(perfil)

# Register your models here.
