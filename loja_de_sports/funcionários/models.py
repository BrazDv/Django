from django.db import models

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome
