from django.db import models

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length = 50)
    sobrenome = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 50)
    bi = models.CharField(max_length =14)


class Carro(models.Model):
    carro = models.CharField(max_length = 50)
    matricula = models.CharField(max_length = 8)
    ano  = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    Lavangens = models.IntegerField(default = 0)
    Reparos = models.IntegerField(default = 0)

class Meta:
    carrro = 'carro'

def __str__(self) -> str:
    return self.carro
