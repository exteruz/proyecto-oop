from django.contrib import admin
from django.urls import path
from .views import get_base,view_index, create_publication, create_book, create_autor, detail_publication
from .views import publications, delete_publication, update_publication
from django.conf import settings
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('base/', get_base.as_view(), name="base"),
    path('', view_index.as_view(), name='inicio'),
    path('crear_publicacion/', create_publication.as_view(), name="crear_publicacion" ),
    path('crear_libro/', create_book.as_view(), name ="crear_libro"),
    path('crear_autor/', create_autor.as_view(), name ="crear_autor"),
    path('ver_publicacion/<int:pk>', detail_publication.as_view(), name ="ver publicacion"),
    path('publicaciones_usuario/', publications.as_view(), name= 'publicaciones_usuario'),
    path('eliminar_publicacion/<int:pk>', delete_publication.as_view(), name='eliminar_publicacion'),
    path('actualizar_publicacion/<int:pk>', update_publication.as_view(), name="actualizar_publicacion")



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)