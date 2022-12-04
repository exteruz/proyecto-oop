from django.views.generic import ListView, TemplateView, CreateView, DetailView,DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import publicacion,libro,autor
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .forms import publicacion_form,crear_libro,crear_autor

from .models import publicacion
class get_base(TemplateView):
    template_name = '../templates/base.html'

class view_index(ListView):
    model = publicacion
    template_name = '../templates/index.html'
    paginate_by = 6

class create_publication(CreateView,LoginRequiredMixin):
    model = publicacion
    form_class = publicacion_form
    template_name = '../templates/create.html'
    success_url = reverse_lazy('inicio')
    
    def form_valid(self, form):
        publicacion = form.save(commit=False)
        publicacion.creador = self.request.user
        publicacion.save()
        return HttpResponseRedirect('../')
    
class create_book (CreateView, LoginRequiredMixin):
    model = libro
    form_class = crear_libro
    template_name = '../templates/create_book.html'
    success_url = HttpResponseRedirect('../crear_publicacion/')
    def form_valid(self, form):
        libro= form.save(commit=False)
        libro.save()
        return HttpResponseRedirect('../crear_publicacion/')

class create_autor(CreateView, LoginRequiredMixin):
    model = autor
    form_class = crear_autor
    template_name = '../templates/create_autor.html'
    def form_valid(self, form):
        libro= form.save(commit=False)
        libro.save()
        return HttpResponseRedirect('../crear_libro/')

class detail_publication(DetailView, LoginRequiredMixin):
    model = publicacion
    template_name = '../templates/detail_publication.html'

class publications(ListView, LoginRequiredMixin):
    model = publicacion
    paginate_by: 6
    template_name = '../templates/user_publications.html'
    def get_queryset(self):
        return publicacion.objects.filter(
            creador=self.request.user
        ).order_by('fecha_publicacion')

class delete_publication(DeleteView, LoginRequiredMixin):
    model = publicacion
    template_name = '../templates/delete.html'
    success_url = reverse_lazy('inicio')
   

class update_publication(UpdateView, LoginRequiredMixin):
    model = publicacion
    form_class = publicacion_form
    template_name = '../templates/create.html'
    success_url = reverse_lazy('publicaciones_usuario')
   