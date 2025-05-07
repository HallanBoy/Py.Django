from django.urls import path

from usuarios import views

urlpatterns = [
  path ('cadastro/', views.criarUsuario, name='cadastro'),

  path('login/', views.login, name='login')
]