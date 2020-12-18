from django.contrib import admin
# Register your models here.
from .models import Genero,Author,Anime

admin.site.register(Anime)
admin.site.register(Author)
admin.site.register(Genero)

