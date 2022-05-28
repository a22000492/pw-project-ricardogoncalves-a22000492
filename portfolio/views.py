from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from matplotlib import pyplot as plt
from .models import Post, PontuacaoQuizz
from .forms import PostForm

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
  agora = datetime.now()
  context = {
      'data': agora.date,
  }

  return render(request, 'portfolio/home.html', context)

def apresentacao_page_view(request):
  return render(request, 'portfolio/apresentacao.html')

def competencias_page_view(request):
  return render(request, 'portfolio/competencias.html')

def formacao_page_view(request):
  return render(request, 'portfolio/formacao.html')

def projetos_page_view(request):
  return render(request, 'portfolio/projetos.html')

def licenciatura_page_view(request):
  return render(request, 'portfolio/licenciatura.html')

def blog_page_view(request):
  form = PostForm(request.POST or None)
  if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
  context = {
      'posts': Post.objects.all(),
      'form': form
  }
  return render(request, 'portfolio/blog.html', context)

def web_page_view(request):
  return render(request, 'portfolio/web.html')

def quizz(request):
  if request.method == 'POST':
    n = request.POST['nome']
    p = pontuacao_quizz(request)
    r = PontuacaoQuizz(nome=n, pontuacao=p)
    r.save()
    desenha_grafico_resultados()

def pontuacao_quizz(request):
  if request.method == 'POST':
    return 3

def desenha_grafico_resultados():
  pontuacoes = sorted(PontuacaoQuizz.objects.all(), key=lambda objeto:objeto.pontuacao, reverse=True)
  nomes_x = []
  pontuacao_y = []
  for nome,pontuacao in pontuacoes:
    nomes_x.append(nome)
    pontuacao_y.append(pontuacao)
  nomes_x.reverse()
  pontuacao_y.reverse()
  plt.barh(nomes_x, pontuacao_y)
  plt.show()
  plt.savefig('static/images/pontuacoes.png ', bbox_inches='tight')
