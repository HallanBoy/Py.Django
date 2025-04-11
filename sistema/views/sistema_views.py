from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) ref ao app sistema
# A função index informa oque vai acontecer quando ela for chamada.

def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )

