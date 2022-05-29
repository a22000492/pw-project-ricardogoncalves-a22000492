from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('sobre', views.sobre_page_view, name='sobre'),
    path('contacto', views.contacto_page_view, name='contacto'),
    path('educacao', views.educacao_page_view, name='educacao'),
    path('projetos', views.projetos_page_view, name='projetos'),
    path('licenciatura', views.licenciatura_page_view, name='licenciatura'),
    path('blog', views.blog_page_view, name='blog'),
    path('web', views.web_page_view, name='web')
]