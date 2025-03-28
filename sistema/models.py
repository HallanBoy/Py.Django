from django.utils import timezone
from django.db import models


# Aqui vai ficar a classe modelo do Usuário
# nome, sobrenome, cpf, telefone, email, foto, endereço.
# data_cadastro, ativo


class Usuario(models.Model):
  nome = models.CharField(max_length=50)
  sobrenome = models.CharField(max_length=50)
  cpf = models.CharField(max_length=11)
  telefone = models.CharField(max_length=20)
  email = models.EmailField()
  endereco = models.CharField(max_length=100)
  data_cadastro = models.DateTimeField(default=timezone.now)
  ativo = models.BooleanField(default=True)
    
  def __str__(self):
    return f"{self.nome} , {self.sobrenome},"

# (Filme -> classe) - nome do filme, ano de lançamento, estudio, genero, sinopse, data de cadastro

# (Genero -> classe) - nome, data de cadastro


class Filme (models.Model):
  nome_filme = models.CharField(max_length=50)
  ano_lancamento = models.DateField(default=timezone.now)
  estudio = models.CharField(max_length=50)
  genero = models.CharField(max_length=10)
  sinopse = models.TextField()
  data_cadastro = models.DateField(default=timezone.now)

  def __str__(self):
    return f"{self.nome_filme}"
  

class Genero (models.Model):
  nome_genero = models.CharField(max_length=20)
  data_cadastro = models.DateField(default=timezone.now)

  def __str__(self):
      return f"{self.nome_genero}"
  