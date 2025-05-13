from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sistema.urls')),
    path('usuario/', include('usuarios.urls')),
    path('filme/', include('filmes.urls')),
]

# 127.0.0.1:8000/ => A página principal
# 127.0.0.1:8000/admin => A página da tela do django admin




