from django.urls import path

from categorias.views import Clase1

urlpatterns = [
    path('categorias', Clase1.as_view())
]