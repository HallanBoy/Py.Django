from django.shortcuts import render, redirect
from sistema.models import Filme
from filmes.forms import FilmeForm

def cadastrarFilme(request):

    if request.method == "POST":
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()   
            return redirect('listar')
    else:
        form = FilmeForm()

    return render(
        request,
        'filmes/cadastrar.html',
        {'form': form},
    )

def listarFilmes(request):
    filmes = Filme.objects.all()
    
    context = {
        'filmes': filmes,
    }
    
    return render(
        request,
        'filmes/listar.html',
        context,
    )
