from django.db import models
from django.utils.text import slugify


class Posts(models.Model):
    slug = models.SlugField(max_length=50, null=False, unique=True, primary_key=True, editable=False)
    titulo = models.CharField("Título", max_length=254, null=False)
    conteudo = models.TextField("Conteúdo", null=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='posts')

    categorias = models.ManyToManyField('core.Categorias', related_name='categorias')
    tags = models.ManyToManyField('core.Tags', related_name='tags')

    created_at = models.DateTimeField('data de criação',auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if len(self.slug) == 0:
            self.slug = slugify(self.titulo)
        super(Posts, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'blog'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
