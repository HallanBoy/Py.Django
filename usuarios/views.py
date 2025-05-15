from django.shortcuts import render, redirect

from usuarios.forms import UsuarioForm

# Create your views here.

def login(request):
    return render(
        request,
        'usuarios/login.html'
    )

def criarUsuario(request):
    # Verificar se a requisição será do tipo GET ou POST
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)    
        # Será criado um objto Usuario(model) com dos dados enviados.
        # post -> São os campos do forms (nome, sobrenome) preenchidos.
        # files -> Contém os arquivos ou e/imagens. 
        if form.is_valid(): # Se os dados forem válidos, são salvos no BD.
            form.save()
            return redirect('usuario/login')
    
    else:
        # Se a requisição for GET, exibir o formulário de cadastro
        form = UsuarioForm()
    
    return render(
        request,
        'usuarios/cadastrar.html',
        {'form': form}
    )