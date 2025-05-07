from django import forms

from sistema.models import Usuario

class UsuarioForm(forms.ModelForm):
  class Meta:
    model = Usuario

    fields = ['nome', 'sobrenome', 'cpf', 'telefone', 'email', 'endereco', 'imagem']