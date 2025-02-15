from django.db import models

# Create your models here.

faixa_choices = (
        ('B', 'Branca'),
        ('A', 'Azul'),
        ('R', 'Roxa'),
        ('M', 'Marrom'),
        ('P', 'Preta')
    )

class Alunos(models.Model):
    
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    faixa = models.CharField(max_length=1, choices=faixa_choices, default='B')
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome
    


class AulasConcluidas(models.Model):
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    faixa_atual = models.CharField(max_length=1, choices=faixa_choices)

    def __str__(self):
        return self.aluno.nome