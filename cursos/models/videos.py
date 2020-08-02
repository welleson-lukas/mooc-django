from django.db import models


class Videos(models.Model):
    videoID = models.SlugField("ID do Vídeo no Youtube", max_length=254, primary_key=True, unique=True)
    titulo = models.CharField("Título", max_length=254, null=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='videos')
    canal = models.ForeignKey('cursos.Canal', on_delete=models.CASCADE, related_name='videos')
    curso = models.ForeignKey('cursos.Cursos', on_delete=models.CASCADE, related_name='videos')

    categorias = models.ManyToManyField('core.Categorias', related_name='videos')
    tags = models.ManyToManyField('core.Tags', related_name='videos')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'cursos'
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
