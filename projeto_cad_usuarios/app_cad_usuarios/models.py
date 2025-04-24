from django.db import models

# MODELS, (OBEJETOS PYTHON, QUE REPRESENTAM UMA TABELA NO BANCO DE DADOS)

class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=245)
    idade = models.IntegerField()

# TRANSFORMAR CODIGO PHYTON EM BANCO DE DADOS
# NO TERMINAL: python .\manage.py makemigrations PARA TRANSFORMAR
#