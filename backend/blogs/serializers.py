# Importaciones
from rest_framework import serializers

from dotenv import load_dotenv

from blogs.models import Blog

import os


class BlogSerializer(serializers.ModelSerializer):

    categoria = serializers.ReadOnlyField(source = "categoria.nombre")
    fecha = serializers.DateTimeField(format = "%d/%m/%Y")

    def get_imagen(self, obj):
        return f"{os.getenv("BASE_URL")}uploads/recetas/{obj.foto}"
    
    class Meta:
        model = Blog
        fields = ('__all__')
