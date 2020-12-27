from django.db import models
from django.utils import timezone

'''
    CONTATOS
    id: INT (automático)
    nome: STR * (obrigatório)
    sobrenome: STR (opcional)
    telefone: STR * (obrigatório)
    email: STR (opcional)
    data_criacao: DATETIME (automático)
    descricao: texto
    categoria: CATEGORIA (outro model)

     CATEGORIA
     id: INT
     nome: STR * (obrigatório)
    '''


class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome

class Contact(models.Model):
    nome = models.CharField(max_length=55)
    sobrenome = models.CharField(max_length=55, blank=True) # optional field.
    telefone = models.CharField(max_length=55)
    email = models.CharField(max_length=55, blank=True) # optional field.
    data_criacao = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True) # optional field
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


'''
NEXT STEPS:
python manage.py makemigrations   (FAZER AS MIGRAÇÕES)
python manage.py migrate          (EXECUTAR ALTERAÇÕES)
'''

'''
IMPORTANT:
Após qualquer alteração deve-se utilizar os 2 comandos acima para
validar as alterações no migrations.
'''



