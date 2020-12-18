from django.views.generic import ListView , FormView , CreateView , DeleteView , UpdateView
from core.Animes.models import Genero
from core.Animes.form import GeneroForm
from django.urls import reverse_lazy


class GenderCreateView(CreateView):
    model = Genero
    form_class = GeneroForm
    template_name = "templatesGenero/createGenero.html"
    success_url = reverse_lazy("anime_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class GenderListView(ListView):
    model = Genero
    template_name = "templatesGenero/listGenero.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["generos"] = Genero.objects.all()
        return context


class GenderUpdateView(UpdateView):
    model = Genero
    form_class = GeneroForm
    template_name = "templateAuthor/createAuthor.html"
    success_url = reverse_lazy("anime_list")

class GenderDeleteView(DeleteView):
    model = Genero
    template_name = "templateAuthor/createAuthor.html"
    success_url = reverse_lazy("anime_list")

