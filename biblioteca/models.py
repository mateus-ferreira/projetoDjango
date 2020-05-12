from django.conf import settings
from django.db import models
from django.utils import timezone


class Livro(models.Model):
	usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
	titulo = models.CharField(max_length=200)
	autor = models.CharField(max_length=200)
	quantidade = models.IntegerField(default='1')
	idioma = models.CharField(choices=(('Português', 'Português'), ('Inglês', 'Inglês'), ('Espanhol', 'Espanhol'), ('Outro', 'Outro')), max_length=15,default='Português')
	codigo = models.CharField(max_length=20)

class Aluno(models.Model):
	nome = models.CharField(max_length=200)
	matricula = models.CharField(max_length=20)
	serie = models.CharField(choices=(('Pré II', 'Pré II'), ('1 Ano', '1 Ano'), ('2 Ano', '2 Ano'), 
		('3 Ano', '3 Ano'), ('4 Ano', '4 Ano'), ('5 Ano', '5 Ano'), ('6 Ano', '6 Ano'), 
		('7 Ano', '7 Ano'), ('8 Ano', '8 Ano'), ('9 Ano', '9 Ano')), max_length=15,default='Pré II')

class Emprestimo(models.Model):
	livro = models.ForeignKey(Livro, on_delete=models.PROTECT)
	aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
	dataEmprestimo = models.DateField()
	dataDevolucao = models.DateField()