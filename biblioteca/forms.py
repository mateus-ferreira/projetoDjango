from django import forms
from .models import Aluno
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import date

class AlunoForm(forms.ModelForm):

	class Meta:

		model = Aluno
		fields = ('nome', 'matricula', 'serie')

	def __init__(self, *args, **kwargs):
		super(AlunoForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.form_method = 'POST'
		self.helper.add_input(Submit('submit', 'Salvar'))