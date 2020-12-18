from django.views.generic import ListView ,  CreateView , UpdateView , DeleteView
from core.Animes.models import Anime, Genero , Author
from core.Animes.form import AnimeForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.shortcuts import render

class ListadoViews(ListView):
    
    model = Anime
    template_name = "listado.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Animes'] = Anime.objects.all()
        context["Generos"] = Genero.objects.all()
        context["Authors"] = Author.objects.all()
        
        return context
    
class AnimeCreateView(CreateView):
    model = Anime
    template_name = "templateAnime/createAnime.html"
    form_class = AnimeForm
    success_url = reverse_lazy("anime_list")


    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST , request.FILES)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request , self.template_name , {"form" : form})


    
class AnimeDeleteView(DeleteView):
    model = Anime
    template_name = "templateAnime/createAnime.html"
    form_class = AnimeForm
    success_url = reverse_lazy("anime_list")


class AnimeUpdateView(UpdateView):
    model = Anime
    template_name = "templateAnime/createAnime.html"
    form_class = AnimeForm
    success_url = reverse_lazy("anime_list")
    

    def post(self, request , *args , **kwargs):
        form = self.form_class(request.POST , request.FILES)

        if form.is_valid:
            form.save()
            return HttpResponseRedirect(self.success_url)
        else:
            return render(request , self.template_name , {"form" : form})

