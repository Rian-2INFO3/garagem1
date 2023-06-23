from django.db import models

# Create your models here.

from django.db import models

class Categoria(models.Model):
    descricao = models.CharField(max_length=100)