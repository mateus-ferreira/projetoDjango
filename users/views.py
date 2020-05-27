from .forms import CustomUserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUp(generic.CreateView):
	form_class = CustomUserCreationForm
	success_url = reverse_lazy('biblioteca:index')
	template_name = 'registration/signup.html'