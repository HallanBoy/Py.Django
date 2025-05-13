from django import forms
from sistema.models import Filme

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = ['nome', 'ano', 'estudio', 'genero', 'sinopse',]