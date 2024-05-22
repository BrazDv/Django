from django.db import models

class Fornecedor(models.Model):
    nome = models.CharField(max_length=100)
    pessoa_contato = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
