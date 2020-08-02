from django.db import models


class Respostas(models.Model):
    conteudo = models.TextField('Conteúdo', null=False)

    topico = models.ForeignKey('forum.Topicos', on_delete=models.CASCADE, related_name='respostas')

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='respostas')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.conteudo

    class Meta:
        app_label = 'forum'
        verbose_name = 'Resposta'
        verbose_name_plural = 'Respostas'
