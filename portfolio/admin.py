from django.contrib import admin

# Register your models here.
from .models import Laboratorio, Post
from .models import Cadeira
from .models import Professor
from .models import Linguagem
from .models import Projeto
from .models import PontuacaoQuizz
from .models import Tfc
from .models import Noticia, Laboratorio

admin.site.register(Post)
admin.site.register(Cadeira)
admin.site.register(Professor)
admin.site.register(Linguagem)
admin.site.register(Projeto)
admin.site.register(PontuacaoQuizz)
admin.site.register(Tfc)
admin.site.register(Noticia)
admin.site.register(Laboratorio)
