from django import forms
from django.forms import ModelForm
from .models import Post


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
