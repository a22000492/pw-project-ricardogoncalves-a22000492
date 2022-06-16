from django.db import models
from django.core.validators import MinValueValidator 

def posts_resolution_path(instance, filename):
    return 'images/{0}/'.format(filename)

class Post(models.Model):
  autor = models.CharField(max_length=100)
  titulo = models.CharField(max_length=200)
  descricao = models.CharField(max_length=500)
  link = models.CharField(max_length=200, blank=True)
  imagem = models.ImageField(upload_to=posts_resolution_path, blank=True)
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.titulo[:50]

class PontuacaoQuizz(models.Model):
  nome = models.CharField(max_length=100)
  pontuacao = models.IntegerField(validators=[MinValueValidator(0)])
  criado = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nome[:50]

class Linguagem(models.Model):
  nome = models.CharField(max_length=50)

  def __str__(self):
    return self.nome[:50]

class Professor(models.Model):
  nome = models.CharField(max_length=20)

  def __str__(self):
    return self.nome[:50]

class Projeto(models.Model):
  nome = models.CharField(max_length=100)
  disciplina = models.CharField(max_length=100, blank=True)
  ano_letivo = models.CharField(max_length=100, blank=True)
  tecnologias = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.nome[:50]

class Cadeira(models.Model):
  nome = models.CharField(max_length=50)
  ano = models.IntegerField()
  descricao = models.TextField()
  linguagens = models.ManyToManyField(Linguagem)
  docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
  docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
  projetos = models.ManyToManyField(Projeto)

  def __str__(self):
    return self.nome[:50]

class Tfc(models.Model):
  autores = models.CharField(max_length=500)
  ano = models.IntegerField()
  titulo = models.CharField(max_length=100)
  resumo = models.TextField()
  imagem = models.ImageField(upload_to=posts_resolution_path, blank=True)
  relatorio = models.CharField(max_length=100, blank=True)
  github = models.CharField(max_length=100, blank=True)
  video = models.CharField(max_length=100, blank=True)

  def __str__(self):
    return self.titulo[:100]

class Noticia(models.Model):
  titulo = models.CharField(max_length=100)
  descricao = models.TextField(max_length=100, blank=True)
  link = models.URLField(max_length=100, blank=True)

  def __str__(self):
    return self.titulo[:50]

class Laboratorio(models.Model):
  titulo = models.CharField(max_length=150)
  descricao = models.TextField(max_length=100, blank=True)
  link = models.URLField(max_length=100, blank=True)

  def __str__(self):
    return self.titulo[:50]
