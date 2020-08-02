from django.db import models
from django.utils.text import slugify


class Niveis(models.Model):
    slug = models.SlugField(max_length=50, null=False, unique=True, primary_key=True, editable=False)
    nome = models.CharField('Nivel', max_length=50, null=False)

    created_at = models.DateTimeField('Data',auto_now_add=True)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.nome)
        super(Niveis, self).save(*args, **kwargs)

    def __str__(self):
        return self.nome

    class Meta:
        app_label = 'questoes'
        verbose_name = 'Nivel'
        verbose_name_plural = 'Niveis'
