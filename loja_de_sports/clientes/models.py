from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    numero_telefone = models.CharField(max_length=15)
    endereco = models.TextField()

    def __str__(self):
        return self.nome
