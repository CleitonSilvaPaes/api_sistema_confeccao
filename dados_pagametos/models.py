from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class DadosPagamentos(models.Model):
    
    banco = models.CharField(max_length=50, blank=True, null=True)
    conta = models.IntegerField(validators=[MaxLengthValidator(8), MinLengthValidator(8)], blank=True, null=True)
    agencia =  models.IntegerField(validators=[MaxLengthValidator(4), MinLengthValidator(4)], blank=True, null=True)
    pix = models.CharField(max_length=50, blank=False, null=False, unique=True)