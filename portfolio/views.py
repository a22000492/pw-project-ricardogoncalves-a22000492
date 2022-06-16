from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime

from matplotlib import pyplot as plt
import io
import urllib, base64
import matplotlib
matplotlib.use('Agg')

from .models import Cadeira, Post, PontuacaoQuizz, Projeto, Tfc, Noticia
from .forms import PostForm, ProjetoForm
from django.shortcuts import redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.shortcuts import render

def view_login(request):

  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(
      request,
      username=username,
      password=password)

    if user is not None:
      login(request, user)
      return HttpResponseRedirect(reverse('portfolio:home'))
    else:
        return render(request, 'portfolio/login.html', {
            'message': 'Credenciais invalidas.'
        })

  return render(request, 'portfolio/login.html')

def view_logout(request):
  logout(request)

  return render(request, 'portfolio/login.html', {
      'message': 'Foi desconetado.'
  })

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
    'projetos': Projeto.objects.all(),
    'tfcs': Tfc.objects.all()
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

def noticias_page_view(request):
  context = {
      'noticias': Noticia.objects.all()
  }
  return render(request, 'portfolio/noticias.html', context)

def quizz_page_view(request):
  if request.method == 'POST':
    nome = request.POST['nome']
    pontos = pontuacao_quizz(request)
    if PontuacaoQuizz.objects.filter(nome=nome).exists():
      PontuacaoQuizz.objects.filter(nome=nome).update(pontuacao=pontos)
    else:
      query = PontuacaoQuizz(nome=nome, pontuacao=pontos)
      query.save()

    return redirect(reverse('portfolio:quizz'))

  context = {
    'data': desenha_grafico_resultados()
  }

  return render(request, 'portfolio/quizz.html', context)

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
  plt.ylabel("Prioridade")
  plt.autoscale()

  fig = plt.gcf()
  plt.close()

  buf = io.BytesIO()
  fig.savefig(buf, format='png')


  buf.seek(0)
  string = base64.b64encode(buf.read())
  uri = urllib.parse.quote(string)

  return uri

def tfc_detail_page_view(request, pk):
  context = {
    'tfc': Tfc.objects.get(pk=pk)
  }
  return render(request, 'portfolio/tfc_detail.html', context)

def apis_page_view(request):
  return render(request, 'portfolio/apis.html')


def novo_projeto_page_view(request):

  if not request.user.is_authenticated:
    return HttpResponseRedirect(reverse('portfolio:login'))

  form = ProjetoForm(request.POST or None)

  if form.is_valid():
    form.save()
    return HttpResponseRedirect(reverse('portfolio:projetos'))

  context = {'form': form}
  return render(request, 'portfolio/novo_projeto.html', context)

@login_required
def editar_projeto_page_view(request, projeto_id):

    projeto = Projeto.objects.get(id=projeto_id)
    form = ProjetoForm(request.POST or None, instance=projeto)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:projetos'))

    context = {'form': form, 'projeto_id': projeto_id}
    return render(request, 'portfolio/editar_projeto.html', context)
