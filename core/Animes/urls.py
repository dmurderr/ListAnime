from django.urls import path
from core.Animes.views.anime.views import ListadoViews 
from core.Animes.views.autor.views import AuthorCreateView , AuthorListView , AuthorUpdateView , AuthorDeleteView
from core.Animes.views.genero.views import GenderCreateView , GenderListView , GenderDeleteView , GenderUpdateView
from core.Animes.views.anime.views import AnimeCreateView , AnimeDeleteView , AnimeUpdateView

urlpatterns = [
    path('listado/', ListadoViews.as_view() , name = "anime_list"),
    path('autor/create/Author/', AuthorCreateView.as_view() , name = "create_Author"),
    path('autor/edit/Author/<int:pk>/', AuthorUpdateView.as_view() , name = "Edit_Author"),
    path('autor/delete/Author/<int:pk>/', AuthorDeleteView.as_view() , name = "delete_Author"),
    path('genero/create/Genero/', GenderCreateView.as_view() , name = "create_Genero"),  
    path('genero/edit/Genero/<int:pk>/', GenderUpdateView.as_view() , name = "edit_Genero"),
    path('genero/delete/Genero/<int:pk>/', GenderDeleteView.as_view() , name = "delete_Genero"),  
    path('createAnime/', AnimeCreateView.as_view() , name = "create_Anime"),
    path('autor/list/', AuthorListView.as_view() , name = "list_Author"),   
    path('genero/list/', GenderListView.as_view() , name = "list_Gender"),   
    path('delete/<int:pk>', AnimeDeleteView.as_view() , name = "delete_Anime"),
    path('update/<int:pk>', AnimeUpdateView.as_view() , name = "update_Anime"),   
]




