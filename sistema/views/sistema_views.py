from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) ref ao App sistema
# A função index informa o que vai acontecer quando ela for chamada.
def index(request):
    return render(
        request,
        'sistema/sistema.html',
    )




# REQUEST
# RESPONSE