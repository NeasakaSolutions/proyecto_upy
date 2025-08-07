# Importaciones
from django.http.response import JsonResponse
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response

from categorias.models import Categoria 
from categorias.serializers import CategoriaSerializer

from http import HTTPStatus

class Clase1(APIView):


    def get(self, request):
        data = Categoria.objects.order_by('-id').all()
        datos_json = CategoriaSerializer(data, many = True)
        return JsonResponse({"data": datos_json.data}, status = HTTPStatus.OK)
    

    def post(self, request):
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


    def get(self, request, id):
        try:
            data = Categoria.objects.filter(id = id).get()
            return JsonResponse({"data": {"id": data.id ,"nombre": data.nombre, "slug": data.slug}},
                             status = HTTPStatus.OK)
        except Categoria.DoesNotExist:
            raise Http404
