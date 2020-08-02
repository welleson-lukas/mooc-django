from django.contrib import admin
from .models import Canal, Cursos, Videos

class FiltroCursos(admin.ModelAdmin):
    list_filter = ["created_at", "categorias"]
    search_fields = ['titulo', 'conteudo']
    list_per_page = 10


admin.site.register(Canal)
admin.site.register(Cursos, FiltroCursos)
admin.site.register(Videos)
