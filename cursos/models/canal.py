from django.db import models


class Canal(models.Model):
    titulo = models.CharField("Título", max_length=254, null=False)
    url = models.URLField("Url do canal", max_length=254, null=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='canais')

    categorias = models.ManyToManyField('core.Categorias', related_name='canais')
    tags = models.ManyToManyField('core.Tags', related_name='canais')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'cursos'
        verbose_name = 'Canal'
        verbose_name_plural = 'Canais'
