from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('usuario/', include('usuarios.urls')),
    path('filmes/', include('filmes.urls')),
]