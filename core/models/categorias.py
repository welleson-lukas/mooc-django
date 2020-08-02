from django.db import models
from django.utils.text import slugify


class Categorias(models.Model):
    slug = models.SlugField(max_length=50, null=False, unique=True, primary_key=True, editable=False)
    nome = models.CharField('Nome da Categoria', max_length=50, null=False)

    created_at = models.DateTimeField('data',auto_now_add=True)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.nome)
        super(Categorias, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'core'
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
