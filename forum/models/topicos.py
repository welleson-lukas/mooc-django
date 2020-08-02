from django.db import models


class Topicos(models.Model):
    titulo = models.CharField("Título do Tópico", max_length=254, null=False)
    conteudo = models.TextField("Conteúdo", null=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='topicos')
    categorias = models.ManyToManyField('core.Categorias', related_name='categorias_topicos')
    tags = models.ManyToManyField('core.Tags', related_name='tags_topicos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'forum'
        verbose_name = 'Topico'
        verbose_name_plural = 'Topicos'
