# Importaciones
from django.http.response import JsonResponse
from django.http import Http404
from django.utils.text import slugify

from rest_framework.views import APIView
from rest_framework.response import Response

from categorias.models import Categoria 
from categorias.serializers import CategoriaSerializer

from http import HTTPStatus

class Clase1(APIView):
    """Manejo de listado y creación de categorías."""

    def get(self, request):
        """Devuelve todas las categorías ordenadas por id descendente."""

        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)
    

    def post(self, request):
        """Crea una nueva categoría si se proporciona el nombre."""
        # Validaciones
        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        try:
            Categoria.objects.create(nombre = request.data['nombre'])
            return JsonResponse({"estado": "ok", "mensaje": "Se creo el registro correctamente"},
                                 status = HTTPStatus.CREATED)
        except Exception as e:
            raise Http404


class Clase2(APIView):
    """Manejo de operaciones CRUD sobre una categoría específica por id."""

    def get(self, request, id):
        """Obtiene la categoría con el id especificado."""

        try:
            data = Categoria.objects.filter(id = id).get()
            return JsonResponse({"data": {"id": data.id ,"nombre": data.nombre, "slug": data.slug}},
                             status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
        

    def put(self, request, id):
        """Actualiza el nombre y slug de la categoría con el id dado."""

        if request.data.get("nombre") == None or not request.data["nombre"]:
            return JsonResponse({"estado": "error", "mensaje" : "El campo nombre es obligatorio"},
                                status = HTTPStatus.BAD_REQUEST)
        
        try:
            data = Categoria.objects.filter(pk = id).get()
            Categoria.objects.filter(pk = id).update(nombre = request.data.get("nombre"),
                                    slug = slugify(request.data.get("nombre")))
            return JsonResponse({"estado": "ok", "mensaje": "Se modifico el registro correctamente"},
                                 status = HTTPStatus.OK)

        except Categoria.DoesNotExist:
            raise Http404
        
    
    def delete(self, request, id):
        """Elimina la categoría con el id especificado."""
         
        try:
            data = Categoria.objects.filter(pk = id).get()
            Categoria.objects.filter(pk = id).delete()
            return JsonResponse({"estado": "ok", "mensaje": "Se elimino el registro correctamente"},
                                 status = HTTPStatus.OK)

        except Categoria.DoesNotExist:
            raise Http404
