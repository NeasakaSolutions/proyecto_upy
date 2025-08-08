# Importaciones
from django.http.response import JsonResponse
from django.http import Http404
from django.utils.text import slugify
from django.utils.dateformat import DateFormat

from rest_framework.views import APIView

from blogs.serializers import BlogSerializer
from blogs.models import Blog

from http import HTTPStatus

from dotenv import load_dotenv

from categorias.models import Categoria

from datetime import datetime

import os


class Clase1(APIView):
    """Lista o crea registros de blogs."""

    def get (self, request):
        """Devuelve todos los blogs ordenados por id descendente."""

        data = Blog.objects.order_by('-id').all()
        datos_json = BlogSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data})
    

    def post(self, request):
        """Crea un nuevo blog con los datos proporcionados."""

        try:
            pdf_file = request.FILES.get('pdf')

            blog = Blog.objects.create(
            nombre = request.data["nombre"],
            descripcion = request.data["descripcion"],
            categoria_id = request.data.get("categoria_id"),
            fecha = datetime.now(),
            foto = "sss",
            pdf = pdf_file
        )

            return JsonResponse({"estado": "ok", "mensaje": "Se creó el registro correctamente"},
                            status=HTTPStatus.CREATED)

        except Exception as e:
            raise Http404

class Clase2(APIView):
    """Obtiene detalles de un blog específico por id."""

    def get (self, request, id):
        """Devuelve la información detallada de un blog."""
        
        try:
            data = Blog.objects.filter(id = id).get()
            base_url = os.getenv("BASE_URL", "")
            imagen_url = f"{base_url}uploads/recetas/{data.foto}" if data.foto else None
            pdf_url = f"{base_url}media/{data.pdf}" if data.pdf else None

            return JsonResponse({ "data": { "id": data.id, "nombre": data.nombre,
                    "slug": data.slug, "descripcion": data.descripcion,
                    "fecha": DateFormat(data.fecha).format('d/m/Y'), "categoria_id": data.categoria_id,
                    "imagen": imagen_url, "pdf": pdf_url}}, status = HTTPStatus.OK)
        
        except Blog.DoesNotExist:
            raise Http404

