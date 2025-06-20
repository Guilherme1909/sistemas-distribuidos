from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Item(models.Model):
    titulo = models.CharField('Titulo', max_length=50)
    descricao = models.TextField('Descricao', max_length=100)
    data_inicio = models.DateTimeField('Data Inicial', auto_now_add=True)
    data_fim = models.DateTimeField('Data Final', null=True)
    valorInicial = models.DecimalField('Valor Inicial', max_digits=10, decimal_places=2, null=True)
    valorAtual = models.DecimalField('Valor Atual', max_digits=10, decimal_places=2, null=True)
    valorFinal = models.DecimalField('Valor Final', max_digits=10, decimal_places=2, null=True)
    imagem = models.ImageField(upload_to='itens/', null=True, blank=True)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
        ordering = ['id']

    def __str__(self):
        return self.titulo


class Lance(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='lances')
    #usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.DecimalField('Valor', max_digits=10, decimal_places=2)
    data = models.DateTimeField('Data', auto_now_add=True)

    class Meta:
        verbose_name = 'Lance'
        verbose_name_plural = 'Lances'
        ordering = ['id']

    def __str__(self):
        return f'Lance de {self.valor}'


@receiver(post_save, sender=Lance)
def atualizar_valor_item(sender, instance, created, **kwargs):
    if created:
        item = instance.item
        if item.valorAtual is None or instance.valor > item.valorAtual:
            item.valorAtual = instance.valor
            item.save()
