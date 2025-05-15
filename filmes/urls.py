from django.urls import path
from filmes import views

urlpatterns = [
    path('cadastrar/', views.cadastrarFilme, name='cadastrarfilme'),
    path('listar/', views.listarFilmes, name='listarfilmes'),
]


