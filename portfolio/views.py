from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from matplotlib import pyplot as plt
from .models import Cadeira, Post, PontuacaoQuizz, Projeto
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
from django.shortcuts import render

def home_page_view(request):
  agora = datetime.now()
  context = {
      'data': agora.date,
  }

  return render(request, 'portfolio/home.html', context)

def sobre_page_view(request):
  return render(request, 'portfolio/sobre.html')

def contacto_page_view(request):
  return render(request, 'portfolio/contacto.html')

def educacao_page_view(request):
  context = {
    'cadeiras': Cadeira.objects.all()
  }
  return render(request, 'portfolio/educacao.html', context)

def projetos_page_view(request):
  context = {
    'projetos': Projeto.objects.all()
  }
  return render(request, 'portfolio/projetos.html', context)

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
  if request.method == 'POST':
    nome = request.POST['nome']
    pontos = pontuacao_quizz(request)
    if PontuacaoQuizz.objects.filter(nome=nome).exists():
      PontuacaoQuizz.objects.filter(nome=nome).update(pontuacao=pontos)
    else:
      query = PontuacaoQuizz(nome=nome, pontuacao=pontos)
      query.save()
    desenha_grafico_resultados()
    return redirect(reverse('portfolio:web'))

  return render(request, 'portfolio/web.html')

def pontuacao_quizz(request):
  pontos = 0
  if request.method == 'POST':
    if request.POST['html'] == 'html1':
      pontos += 15
    if request.POST['image-tag'] == 'image-tag3':
      pontos += 15
    if request.POST['python'] == 'python2':
      pontos += 15
    return pontos

def desenha_grafico_resultados():
  query = sorted(PontuacaoQuizz.objects.all(),
                  key=lambda x: x.pontuacao, reverse=True)
  nomes = [objeto.nome for objeto in query]
  pontuacoes = [objeto.pontuacao for objeto in query]
  plt.barh(nomes, pontuacoes)
  plt.savefig('portfolio/static/portfolio/images/pontuacoes.png',
              bbox_inches='tight')
  plt.close()
