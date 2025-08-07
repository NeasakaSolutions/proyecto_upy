# Importaciones
from django.db import models

from autoslug import AutoSlugField

class Categoria(models.Model):
    '''Clase que representa el modelo de la base de datos'''

    nombre = models.CharField(max_length = 100, null = False)
    slug = AutoSlugField(populate_from = 'nombre')

    def __str__(self):
        ''' Campo que mostrara '''
        return self.nombre
    
    class Meta:
        '''Nombres para el administrador de django'''
        db_table = 'categorias'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
