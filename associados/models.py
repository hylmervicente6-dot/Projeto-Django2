from django.db import models
from tinymce.models import HTMLField

class Autor(models.Model):
    # atributo
    # o atributo id e automático.
    # chave primária imutavel, universal e única
    nome = models.CharField(max_length=100)
    biografia = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'autor'



class EixoTecnologia(models.Model):
    id = models
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
    class Meta:
        db_table = 'eixo'

class Artigo(models.Model):
    texto = HTMLField()
    data_publicacao = models.DateTimeField(auto_now_add=True)
    id_fk_eixo = models.ForeignKey(
        EixoTecnologia,
        on_delete=models.CASCADE,
        db_column='id_fk_eixo'
    )
    id_fk_autor = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        db_column='id_fk_autor'
    )

    def __str__(self):
        return f"Artigo {self.id} - {self.data_publicacao}"
    
    class Meta:
        db_table = 'artigo'

      
          

