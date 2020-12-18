from django.db import models
from django.contrib.auth.models import AbstractUser   
from core.Animes.models import Anime
# Create your models here.


class User(AbstractUser):
    selection_anime = models.ManyToManyField(Anime, verbose_name="Seleciona Animes")
