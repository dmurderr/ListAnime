from django.views.generic import ListView , FormView , CreateView , DeleteView , UpdateView
from core.Animes.models import Author
from core.Animes.form import autorForm
from django.urls import reverse_lazy


class AuthorCreateView(CreateView):
    model = Author
    form_class = autorForm
    template_name = "templateAuthor/createAuthor.html"
    success_url = reverse_lazy("anime_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AuthorListView(ListView):
    model = Author
    template_name = "templateAuthor/listAuthor.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["autores"] = Author.objects.all()
        return context
    
    
class AuthorUpdateView(UpdateView):
    model = Author
    form_class = autorForm
    template_name = "templateAuthor/createAuthor.html"
    success_url = reverse_lazy("anime_list")

class AuthorDeleteView(DeleteView):
    model = Author
    form_class = autorForm
    template_name = "templateAuthor/createAuthor.html"
    success_url = reverse_lazy("anime_list")

