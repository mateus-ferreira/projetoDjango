from django.urls import path
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrarAluno', views.cadastrarAluno, name='cadastrarAluno'),
]