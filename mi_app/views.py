from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DeleteView, UpdateView
from .models import Item
from django.http import Http404, HttpResponseBadRequest
from django.utils import timezone

class ItemListView(TemplateView):
    template_name = 'mi_app/template.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context

class ItemCreateView(CreateView):
    model = Item
    fields = []
    success_url = reverse_lazy('listar_items')

    def form_valid(self, form):
        # Generar una marca de tiempo en formato "YY-MM-dd hh:mm"
        fecha_hora_actual = timezone.now()
        nombre = fecha_hora_actual.strftime("%y-%m-%d %H:%M")

        # Validar que el nombre no se repita
        if Item.objects.filter(nombre=nombre).exists():
            messages.error(self.request, "El elemento con este nombre ya existe.")
            return redirect(self.success_url)

        form.instance.nombre = nombre
        return super().form_valid(form)

class ItemUpdateView(UpdateView):
    model = Item
    fields = ['nombre']
    template_name = 'mi_app/item_form.html'  # Reutiliza la misma plantilla que para la creación
    success_url = reverse_lazy('listar_items')

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('listar_items')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        estado_nuevo = request.POST.get('estado', 'Activado')

        if self.object.estado == 'Eliminado' and estado_nuevo == 'Activado':
            raise Http404("No se puede activar un elemento eliminado")

        self.object.estado = estado_nuevo
        self.object.save()
        return redirect(self.success_url)