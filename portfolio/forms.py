from django import forms
from django.forms import ModelForm
from .models import Post, Projeto, Cadeira


class PostForm(ModelForm):
  class Meta:
    model = Post
    fields = '__all__'
    widgets = {
      'titulo': forms.TextInput(),
      'autor': forms.TextInput(),
      'descricao': forms.Textarea(),
      'imagem': forms.FileInput(),
      'link': forms.URLInput(),
    }
    labels = {
      'autor': 'Autor',
      'titulo': 'Título',
      'descricao': 'Texto',
      'link': 'Link',
      'imagem': 'Imagem'
    }

    help_texts = {
    }

class ProjetoForm(ModelForm):
  class Meta:
    model = Projeto
    fields = '__all__'
    widgets = {
      'nome': forms.TextInput(),
      'disciplina': forms.TextInput(),
      'ano_letivo': forms.TextInput(),
      'tecnologias': forms.TextInput(),
    }
    labels = {
      'nome': 'Nome',
      'disciplina': 'Disciplina',
      'ano_letivo': 'Ano Letivo',
      'tecnologias': 'Tecnologias'
    }

    help_texts = {
    }

class CadeiraForm(ModelForm):
  class Meta:
    model = Cadeira
    fields = '__all__'
    widgets = {
    }
    labels = {
    }
    help_texts = {
    }