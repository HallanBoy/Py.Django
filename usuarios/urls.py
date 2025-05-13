from django.urls import path
from usuarios import views

urlpatterns = [
    path('cadastro/', views.criarUsuario, name='criarUsuario'),
    path('login/', views.login, name='login'),
]

# 127.0.0.1:8000/usuario
# 127.0.0.1:8000/usuario/login
# 127.0.0.1:8000/usuario/cadastro
