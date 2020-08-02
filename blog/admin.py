from django.contrib import admin
from .models import Posts

class FiltrosPost(admin.ModelAdmin):
    list_filter = ["created_at", "categorias"]
    search_fields = ['titulo', 'conteudo']
    list_per_page = 10


admin.site.register(Posts, FiltrosPost)
