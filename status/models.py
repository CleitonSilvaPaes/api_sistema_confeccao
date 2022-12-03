from django.db import models

class Status(models.Model):
    STATUS = (
        ('N', 'Novo'),
        ('I', 'Iniciado'),
        ('F', 'Finalizado'),
        ('E', 'Entrege')
    )
    status = models.CharField(max_length=1, choices=STATUS, blank=False, null=False, default='N')
    data_criado = models.DateTimeField(auto_now=True, auto_now_add=False)
    data_modificado = models.DateTimeField(auto_now=False, auto_now_add=True)