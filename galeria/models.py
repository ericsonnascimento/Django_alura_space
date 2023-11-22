from django.db import models
from datetime import datetime

class Fotografia(models.Model):
    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALAXIA', 'Galáxia'),
        ('PLANETA', 'Planeta')
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=50, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='foto/%Y/%m/%d', null=True, blank=True)
    publicada = models.BooleanField(default=False)
    data_publicacao = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome

