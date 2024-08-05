from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

# Create your models here.
class Pessoa(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    profissao = models.CharField(max_length=100, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True, default=None)
    nationality = models.CharField(max_length=64, default="Moçambique")
    province = models.CharField(max_length=64, default="Maputo")
    bi = models.CharField(max_length=14)
    city = models.CharField(max_length=128, default="Matola")
    contact = models.CharField(max_length=32, blank=True)
    joined_in = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
       return f"{self.nome} {self.sobrenome}"
