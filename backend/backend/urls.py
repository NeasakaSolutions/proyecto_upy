# Importaciones:
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('api/v1/', include('categorias.urls')),
    path('api/v1/', include('blogs.urls')),
]

# Url para configuracion de los archivos que se van a mostrar
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
