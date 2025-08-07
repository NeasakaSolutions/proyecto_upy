# Importaciones
from rest_framework import serializers

from categorias.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    """Serializador para el modelo Categoria."""

    class Meta:
        """Define el modelo y los campos a serializar."""
        model = Categoria
        fields = ("id", "nombre", "slug")
