from django.urls import path
from sistema import views

# Informa qual será a rotá que irá chamar determinada view (função)
urlpatterns = [
    path('', views.index),
 #   path('sistema/', views.index),
    path('listar/', views.listarUsuarios),
 #  path('listar_filmes/', views.listarFilmes),
]
urlpatterns = [
    path('', views.index),
 #  path('sistema/', views.index),
 #   path('listar/', views.listarUsuarios),
    path('listar_filmes/', views.listarFilmes),
]