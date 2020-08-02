from django.db import models


class Perguntas(models.Model):
    titulo = models.CharField("Título da pergunta", max_length=254, null=False)
    conteudo = models.TextField("Conteúdo", null=False)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='perguntas')
    assunto = models.ManyToManyField('Assuntos', related_name='assunto')
    niveis = models.ManyToManyField('Niveis', related_name='niveis')

    created_at = models.DateTimeField('data',auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        app_label = 'questoes'
        verbose_name = 'Pergunta'
        verbose_name_plural = 'Perguntas'
