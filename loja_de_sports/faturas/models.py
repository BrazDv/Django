from django.db import models
from clientes.models import Cliente

class faturas(models.Model):
    numero_fatura = models.CharField(max_length=100)
    data = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"Fatura {self.numero_fatura}"
