from django.urls import path


urlpatterns = [
    path("", ListadoViews.as_view(), name="Inicio")
]
