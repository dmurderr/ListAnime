from django import forms 
from core.Animes.models import Author , Genero , Anime

class autorForm(forms.ModelForm):
    
    class Meta:
        model = Author
        fields = '__all__'


class GeneroForm(forms.ModelForm):
    
    class Meta:
        model = Genero
        fields = '__all__'

class AnimeForm(forms.ModelForm):
    
    class Meta:
        model = Anime
        fields = '__all__'