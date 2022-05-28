from django.db import models
from django.core.validators import MinValueValidator 

# Create your models here.

class Post(models.Model):
  autor = models.CharField(max_length=100)
  titulo = models.CharField(max_length=200)
  descricao = models.CharField(max_length=500)
  link = models.CharField(max_length=200, blank=True)
  imagem = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, blank=True)
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo[:50]

class PontuacaoQuizz(models.Model):
  nome = models.CharField(max_length=100)
  pontuacao = models.IntegerField(validators=[MinValueValidator(2)])
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nome[:50]

class Linguagem(models.Model):
  nome = models.CharField(max_length=20)

  def __str__(self):
    return self.nome[:50]

class Professor(models.Model):
  nome = models.CharField(max_length=20)

  def __str__(self):
    return self.nome[:50]

class Projeto(models.Model):
  nome = models.CharField(max_length=20)

  def __str__(self):
    return self.nome[:50]

class Cadeira(models.Model):
  nome = models.CharField(max_length=20)
  ano = models.IntegerField()
  descricao = models.TextField()
  linguagens = models.ManyToMany(Linguagem)
  docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
  docentes_praticas = models.ManyToMany(Professor, related_name='caderias')
  projetos = models.ManyToMany(Projeto)

  def __str__(self):
    return self.nome[:50]
