from django.shortcuts import render, get_object_or_404
from associados.models import Autor, EixoTecnologia, Artigo

def index(request):
    eixos = EixoTecnologia.objects.all()
    return render(request, 'associados/index.html', {'eixos': eixos})

def artigo(request):
    artigos = Artigo.objects.select_related('id_fk_eixo', 'id_fk_autor').all()
    return render(request, 'associados/artigo.html', {'artigos': artigos})

def eixo_detalhe(request, eixo_id):
    eixo = get_object_or_404(EixoTecnologia, id=eixo_id)
    artigos = Artigo.objects.filter(id_fk_eixo=eixo).select_related('id_fk_autor')
    return render(request, 'associados/eixo_detalhe.html', {
        'eixo': eixo,
        'artigos': artigos,
    })

def autores(request):
    lista = Autor.objects.all()
    return render(request, 'associados/autores.html', {'autores': lista})
