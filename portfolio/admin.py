from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Cadeira
from .models import Professor
from .models import Linguagem

admin.site.register(Post)
admin.site.register(Cadeira)
admin.site.register(Professor)
admin.site.register(Linguagem)