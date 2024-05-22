from django.db import models

class produtos(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade_disponivel = models.IntegerField()
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
