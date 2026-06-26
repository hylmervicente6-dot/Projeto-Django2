# boa prática
# cada app se vira com suas rotas
from django.urls import path
from associados.views import index, artigo, eixo_detalhe, autores

urlpatterns = [
    path('', index, name='index'),
    path('artigo/', artigo, name='artigo'),
    path('eixo/<int:eixo_id>/', eixo_detalhe, name='eixo_detalhe'),
    path('autores/', autores, name='autores'),
]