from django.contrib import admin
from .models import Perguntas, Niveis, Assuntos

class FiltroPerguntas(admin.ModelAdmin):
    list_filter = ["created_at", "assunto", "niveis"]
    search_fields = ['titulo', 'conteudo']
    list_per_page = 10

admin.site.register(Perguntas, FiltroPerguntas)
admin.site.register(Niveis)
admin.site.register(Assuntos)
