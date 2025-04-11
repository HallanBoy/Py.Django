from django.contrib import admin

from sistema import models

# Aqui fica o registro do Usuário
@admin.register(models.Usuario)
class UsuarioAdmin(admin.ModelAdmin):
  list_display = ('id','nome','sobrenome','email','ativo',)


@admin.register(models.Filme)
class UsuarioAdmin(admin.ModelAdmin):
  list_display = ('id', 'nome', 'ano_lancamento', 'estudio', 'genero', 'sinopse', 'data_cadastro',)

@admin.register(models.Genero)
class UsuarioAdmin(admin.ModelAdmin):
  list_display = ('id', 'nome', 'data_cadastro',)