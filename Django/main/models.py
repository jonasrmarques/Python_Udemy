from django.db import models

# Create your models here.

class Aluno(models.Model):
    
    nome = models.CharField(max_length=50) #max_length é obrigatório
    email = models.EmailField(blank=True, null=True) #Permite que os dados no banco, sejam nulos ou vazios
    descricao = models.TextField(blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome