from django.shortcuts import get_object_or_404, render, redirect
from .models import Aluno, Livro, Emprestimo
from .forms import AlunoForm, LivroForm, EmprestimoForm
from django.contrib.auth.decorators import login_required
from datetime import datetime
from datetime import date

def index(request):
	nLivros = Livro.objects.count()
	nAlunos = Aluno.objects.count()
	nEmprestimos = Emprestimo.objects.count()
	return render(request, 'biblioteca/index.html', {'nlivros':nLivros, 'nalunos':nAlunos, 'nemprestimos':nEmprestimos})

@login_required
def cadastrarAluno(request):
	if request.method == "POST":
		aluno = AlunoForm(request.POST)
		if aluno.is_valid():
			alunoSalvar = aluno.save(commit=False)
			alunoSalvar.save()
			return redirect('biblioteca:index')
	formAluno = AlunoForm()
	return render(request, 'biblioteca/cadastrarAluno.html', {'form':formAluno})

@login_required
def cadastrarLivro(request):
	if request.method == 'POST':
		livro = LivroForm(request.POST) 
		if livro.is_valid():
			livroSalvar = livro.save(commit=False)
			livroSalvar.save()
			return redirect('biblioteca:index')
	formLivro = LivroForm()
	return render(request, 'biblioteca/cadastrarLivro.html', {'form':formLivro})

@login_required
def cadastrarEmprestimo(request):
	if request.user.is_authenticated:
		livros = Livro.objects.all()
		alunos = Aluno.objects.all()

		if request.method == 'POST':
			cadastro = EmprestimoForm(request.POST)
			
			if cadastro.is_valid():
				cadastroSalvar = cadastro.save(commit=False)
				cadastroSalvar.livro = Livro.objects.get(titulo=dict(cadastro.fields['livros'].choices)[cadastro.cleaned_data['livros']])
				cadastroSalvar.aluno = Aluno.objects.get(nome=dict(cadastro.fields['alunos'].choices)[cadastro.cleaned_data['alunos']])
				cadastroSalvar.save()
				return redirect('biblioteca:index')
		empForm = EmprestimoForm()
		return render(request, 'biblioteca/cadastrarEmprestimo.html', {'form':empForm, 'livros':livros, 'alunos':alunos})
	else:
		return redirect('login')

def exibirAlunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'biblioteca/exibirAlunos.html', {'alunos':alunos})


def exibirLivros(request):
	livros = Livro.objects.all()
	return render(request, 'biblioteca/exibirLivros.html', {'livros':livros})

def exibirEmprestimos(request):
	emprestimos = Emprestimo.objects.all()
	class emps:
		def __init__(self, aluno, livro, emprestimo):

			self.aluno = aluno
			self.livro = livro
			self.emprestimo = emprestimo

	empLivros = []


	hoje = date.today()
	multa = hoje.strftime('%Y-%m-%d')

	for emp in emprestimos:
		aluno = Aluno.objects.get(matricula=emp.aluno.matricula)
		livro = Livro.objects.get(codigo=emp.livro.codigo)
		emprestimo = emp

		mes = str(emprestimo.dataDevolucao)
		

		if multa < mes:
			emprestimo.vencimento = False
		else:
			emprestimo.vencimento = True

		empGeral = emps(aluno, livro, emprestimo)
		empLivros.append(empGeral)

	return render(request, 'biblioteca/exibirEmprestimos.html', {'emprestimos':empLivros})

@login_required
def editarAluno(request, pk):
	alunoEdit = get_object_or_404(Aluno, pk=pk)
	if request.method == "POST":
		form = AlunoForm(request.POST, instance=alunoEdit)
		if form.is_valid():
			alunoEdit = form.save(commit=False)
			alunoEdit.save()
			return redirect('biblioteca:exibirAlunos')
	else:
		form = AlunoForm(instance=alunoEdit)
	return render(request, 'biblioteca/editarAluno.html', {'form':form})

@login_required
def removerAluno(request, pk):
	aluno = get_object_or_404(Aluno, pk=pk)
	aluno.delete()
	return redirect('biblioteca:exibirAlunos')