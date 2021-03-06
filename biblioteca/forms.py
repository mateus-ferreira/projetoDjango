from django import forms
from .models import Aluno, Livro, Emprestimo
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date
from django.utils import timezone

class AlunoForm(forms.ModelForm):

	class Meta:

		model = Aluno
		fields = ('nome', 'matricula', 'serie')

	def __init__(self, *args, **kwargs):
		super(AlunoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Salvar'))

class LivroForm(forms.ModelForm):

	class Meta:

		model = Livro
		fields = ('titulo', 'autor', 'quantidade', 'idioma', 'codigo')

	def __init__(self, *args, **kwargs):
		super(LivroForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Salvar'))

class EmprestimoForm(forms.ModelForm):
	livros = forms.ChoiceField(choices=[(livro.codigo, livro.titulo) for livro in Livro.objects.all()])
	alunos = forms.ChoiceField(choices=[(aluno.matricula, aluno.nome) for aluno in Aluno.objects.all()])
	dataEmprestimo = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))
	dataDevolucao = forms.CharField(widget=forms.widgets.DateTimeInput(attrs={"type": "date"}))

	class Meta:

		model = Emprestimo
		fields = ('dataEmprestimo', 'dataDevolucao')
		exclude = ('livro', 'aluno', )

	def __init__(self, *args, **kwargs):
		super(EmprestimoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Salvar'))