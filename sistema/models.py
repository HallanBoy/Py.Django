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
    imagem = models.ImageField(blank=True, upload_to='imagens/%Y/%m')

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'
    
class Genero(models.Model):
    nome = models.CharField(max_length=50)
    data_cadastro = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.nome

class Filme(models.Model):
    nome = models.CharField(max_length=50)
    ano = models.DateField(default=timezone.now)
    estudio = models.CharField(max_length=50)
    # genero = models.CharField(max_length=50)
    genero = models.ForeignKey(Genero, on_delete=models.SET_NULL, null=True, blank=True)
    sinopse = models.TextField()
    data_cadastro = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nome
    



# Filme - Nome do Filme, ano de lançamento, estúdio, gênero, sinopse, data de cadastro
# Gênero - nome, data de cadastro.

# PK -> Primary key -> Chave primária.
# FK -> Foreign Key -> Chave estrangeira.
