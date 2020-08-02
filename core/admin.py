from django.contrib import admin
from .models import Categorias, Tags


class FiltroCategorias(admin.ModelAdmin):
    list_filter = ["created_at"]
    search_fields = ['nome', ]
    list_per_page = 10

class FiltroTags(admin.ModelAdmin):
    list_filter = ["created_at"]
    search_fields = ['nome', ]
    list_per_page = 10

admin.site.register(Categorias, FiltroCategorias)
admin.site.register(Tags, FiltroTags)
admin.site.site_header = 'Painel de Administração Django'