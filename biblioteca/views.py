from django.shortcuts import render
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Aluno, Livro, Emprestimo
from .forms import AlunoForm, LivroForm, EmprestimoForm

def index(request):
    return render(request, 'biblioteca/index.html', {})

def cadastrarAluno(request):
	if request.method == "POST":
		aluno = AlunoForm(request.POST)
		if aluno.is_valid():
			alunoSalvar = aluno.save(commit=False)
			alunoSalvar.save()
			return redirect('biblioteca:index')
	formAluno = AlunoForm()
	return render(request, 'biblioteca/cadastrarAluno.html', {'form':formAluno})

def cadastrarLivro(request):
	if request.method == 'POST':
		livro = LivroForm(request.POST)
		if livro.is_valid():
			livroSalvar = livro.save(commit=False)
			livroSalvar.save()
			return redirect('biblioteca:index')
	formLivro = LivroForm()
	return render(request, 'biblioteca/cadastrarLivro.html', {'form':formLivro})

def cadastrarEmprestimo(request):
	livros = Livro.objects.all()
	alunos = Aluno.objects.all()

	if request.method == 'POST':
		cadastro = EmprestimoForm(request.POST)
		if cadastro.is_valid():
			cadastroSalvar = cadastro.save(commit=False)
			cadastroSalvar.save()
			return redirect('biblioteca:index')
	empForm = EmprestimoForm()
	return render(request, 'biblioteca/cadastrarEmprestimo.html', {'form':empForm, 'livros':livros, 'alunos':alunos})	

def exibirAlunos(request):
	alunos = Aluno.objects.all()
	return render(request, 'biblioteca/exibirAlunos.html', {'alunos':alunos})


def exibirLivros(request):
	livros = Livro.objects.all()
	return render(request, 'biblioteca/exibirLivros.html', {'livros':livros})

def exibirEmprestimos(request):
	emprestimos = Emprestimo.objects.all()
	return render(request, 'biblioteca/exibirEmprestimos.html', {'emprestimos':emprestimos})	