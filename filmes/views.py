from django.shortcuts import render, redirect

from filmes.forms import FilmeForm

def cadastrarFilme(request):
    if request.method == 'POST':
        form = FilmeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_filmes')  # Nome da URL de listagem
    else:
        form = FilmeForm()
    
    return render(request, 'filmes/cadastrar_filme.html', {'form': form})

