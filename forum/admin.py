from django.contrib import admin
from .models import Respostas, Topicos

class FiltroTopicos(admin.ModelAdmin):
    list_filter = ["created_at", "categorias"]
    search_fields = ['titulo', 'conteudo']
    list_per_page = 10

class FiltroRespostas(admin.ModelAdmin):
    list_filter = ["created_at"]
    list_per_page = 10


admin.site.register(Topicos, FiltroTopicos)
admin.site.register(Respostas, FiltroRespostas)
