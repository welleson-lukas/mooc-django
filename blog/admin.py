from django.contrib import admin
from .models import Posts

class FiltrosPost(admin.ModelAdmin):
    list_filter = ["created_at", "categorias"]
    search_fields = ['titulo', 'conteudo']
    list_per_page = 10


def form_valid(self, form):
    # Define o usuário como usuário logado

    form.instance.user = self.request.user

    url = super().form_valid(form)

    return url
admin.site.register(Posts, FiltrosPost)
