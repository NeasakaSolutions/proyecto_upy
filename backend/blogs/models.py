# Importaciones
from django.db import models

from autoslug import AutoSlugField

from categorias.models import Categoria

class Blog(models.Model):
    """
    Modelo que representa una entrada de blog.

    Atributos:
        categoria (ForeignKey): Categoría asociada al blog.
        nombre (str): Nombre del blog.
        slug (str): Texto amigable para URLs generado automáticamente desde nombre.
        foto (str): Ruta o URL de la foto (opcional).
        descripcion (str): Descripción del blog.
        fecha (datetime): Fecha de última actualización automática.
    """

    categoria = models.ForeignKey(Categoria, models.DO_NOTHING, default = 1)
    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre', max_length = 100)
    foto = models.CharField(max_length = 100, null = True)
    descripcion = models.TextField()
    fecha = models.DateTimeField(auto_now = True)
    pdf = models.FileField(upload_to='pdfs/', null=True, blank=True)

    def __str__(self):
        """Devuelve el nombre del blog como representación del objeto."""

        return self.nombre
    

    class Meta:
        db_table = 'blogs'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'


