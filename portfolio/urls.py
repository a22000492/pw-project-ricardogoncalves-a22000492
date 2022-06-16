from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('apis', views.apis_page_view, name='apis'),
    path('tfc/<int:pk>', views.tfc_detail_page_view, name='tfc_detail'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('novo_projeto', views.novo_projeto_page_view, name='novo_projeto'),
    path('editar_projeto/<int:projeto_id>', views.editar_projeto_page_view, name='editar_projeto'),
    path('nova_cadeira', views.nova_cadeira_page_view, name='nova_cadeira'),
    path('editar_cadeira/<int:cadeira_id>', views.editar_cadeira_page_view, name='editar_cadeira'),
    path('noticias', views.noticias_page_view, name='noticias'),
    path('laboratorios', views.laboratorios_page_view, name='laboratorios'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('login/', views.view_login, name='login'),
    path('logout/', views.view_logout, name='logout')
]